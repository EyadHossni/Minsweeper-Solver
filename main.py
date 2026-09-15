import pygame
import random
from game_solver import solve


def game_drawer(first_time=False):
    pos_counter = [0, 0]
    square_X = square_size * space_relation
    for i in range(game_size):
        square_Y = square_size * space_relation
        pos_counter[1] = 0
        for e in range(game_size):

            block_code_letter = playing_grid[pos_counter[1]][pos_counter[0]]
            text_color = closed_square_color

            if block_code_letter == "M" or block_code_letter == "X":
                color = mines_color
                block_code_letter = ""
            elif block_code_letter == "#":
                color = closed_square_color
                block_code_letter = ""
            else:
                color = open_square_color
                if block_code_letter == 0:
                    block_code_letter = ""
                elif block_code_letter == 1:
                    text_color = number1_color
                elif block_code_letter == 2:
                    text_color = number2_color
                elif block_code_letter == 3:
                    text_color = number3_color
                elif block_code_letter == 4:
                    text_color = number4_color
                elif block_code_letter == 5:
                    text_color = number5_color
                elif block_code_letter == 6:
                    text_color = number6_color

            if first_time or playing_grid[pos_counter[1]][pos_counter[0]] != "#":
                pygame.draw.rect(screen, color, pygame.Rect(square_X, square_Y, square_size, square_size))
                if block_code_letter != "":
                    text = pygame.font.Font("freesansbold.ttf", int(square_size)).render(str(block_code_letter), True, text_color)
                    textX = square_X + (square_size - text.get_size()[0])/2
                    textY = square_Y + (square_size - text.get_size()[1])/2
                    screen.blit(text, (textX, textY))

            if game_over:
                pygame.display.flip()

            square_Y += square_size * space_relation + square_size
            pos_counter[1] = pos_counter[1] + 1
        square_X += square_size * space_relation + square_size
        pos_counter[0] = pos_counter[0] + 1
    pygame.display.flip()


def game_grid_prep():
    global mines_secret_grid
    for i in range(mines):
        put_mine = False
        while not put_mine:
            randomX = random.randint(0, game_size - 1)
            randomY = random.randint(0, game_size - 1)
            if mines_secret_grid[randomY][randomX] == "#":
                mines_secret_grid[randomY][randomX] = "M"
                put_mine = True

    for y in range(game_size):
        for x in range(game_size):
            if mines_secret_grid[y][x] != "M":
                num = mines_counter(mines_secret_grid, x, y)
                mines_secret_grid[y][x] = num


def mines_counter(grid, x, y):
    global playing_grid, game_over
    num = 0
    if y > 0 and grid[y - 1][x] == "M":
        if mines_secret_grid[y - 1][x] == "M":
            num += 1
        else:
            print("game_over")
            game_over = True
            game_drawer()
            return None

    if x > 0 and grid[y][x - 1] == "M":
        if mines_secret_grid[y][x - 1] == "M":
            num += 1
        else:
            print("game_over")
            game_over = True
            game_drawer()
            return None
    if y < game_size - 1 and grid[y + 1][x] == "M":
        if mines_secret_grid[y + 1][x] == "M":
            num += 1
        else:
            print("game_over")
            game_over = True
            game_drawer()
            return None
    if x < game_size - 1 and grid[y][x + 1] == "M":
        if mines_secret_grid[y][x + 1] == "M":
            num += 1
        else:
            print("game_over")
            game_over = True
            game_drawer()
            return None

    if x > 0 and y > 0 and grid[y - 1][x - 1] == "M":
        if mines_secret_grid[y - 1][x - 1] == "M":
            num += 1
        else:
            print("game_over")
            game_over = True
            game_drawer()
            return None

    if x < game_size - 1 and y > 0 and grid[y - 1][x + 1] == "M":
        if mines_secret_grid[y - 1][x + 1] == "M":
            num += 1
        else:
            print("game_over")
            game_over = True
            game_drawer()
            return None
    if x > 0 and y < game_size - 1 and grid[y + 1][x - 1] == "M":
        if mines_secret_grid[y + 1][x - 1] == "M":
            num += 1
        else:
            print("game_over")
            game_over = True
            game_drawer()
            return None
    if x < game_size - 1 and y < game_size - 1 and grid[y + 1][x + 1] == "M":
        if mines_secret_grid[y + 1][x + 1] == "M":
            num += 1
        else:
            print("game_over")
            game_over = True
            game_drawer()
            return None

    return num

def drawer(drawing: list):
    for i in drawing:
        for e in i:
            print(e, end=" ")
        print("")


def mouse_square_finder():
    global mouse_pos, mouse_squareX, mouse_squareY
    mouseX = mouse_pos[0]
    mouseY = mouse_pos[1]

    mouse_squareX = int((mouseX - (square_size*space_relation)/2) / (square_size + space_relation*square_size))
    mouse_squareY = int((mouseY - (square_size*space_relation)/2) / (square_size + space_relation*square_size))

    return [mouse_squareY, mouse_squareX]


def clicker(Closed_square=True):
    global playing_grid, game_over
    if Closed_square:
        if mines_secret_grid[mouse_squareY][mouse_squareX] == "M":
            print("game_over")
            game_over = True
            game_drawer()
        else:
            self_and_around_opener(mouse_squareX, mouse_squareY)

    else:
        number = playing_grid[mouse_squareY][mouse_squareX]
        found_number = mines_counter(playing_grid, mouse_squareX, mouse_squareY)
        if found_number == number:
            self_and_around_opener(mouse_squareX, mouse_squareY)



def self_and_around_opener(openX, openY):
    global playing_grid
    new_points = []
    playing_grid[openY][openX] = mines_secret_grid[openY][openX]

    if openY > 0 and playing_grid[openY - 1][openX] == "#":
        if mines_secret_grid[openY - 1][openX] == 0:
            new_points.append([openX, openY - 1])
        elif mines_secret_grid[openY - 1][openX] != "M":
            playing_grid[openY - 1][openX] = mines_secret_grid[openY - 1][openX]

    if openX > 0 and playing_grid[openY][openX - 1] == "#":
        if mines_secret_grid[openY][openX - 1] == 0:
            new_points.append([openX - 1, openY])
        elif mines_secret_grid[openY][openX - 1] != "M":
            playing_grid[openY][openX - 1] = mines_secret_grid[openY][openX - 1]

    if openY < game_size - 1 and playing_grid[openY + 1][openX] == "#":
        if mines_secret_grid[openY + 1][openX] == 0:
            new_points.append([openX, openY + 1])
        elif mines_secret_grid[openY + 1][openX] != "M":
            playing_grid[openY + 1][openX] = mines_secret_grid[openY + 1][openX]

    if openX < game_size - 1 and playing_grid[openY][openX + 1] == "#":
        if mines_secret_grid[openY][openX + 1] == 0:
            new_points.append([openX + 1, openY])
        elif mines_secret_grid[openY][openX + 1] != "M":
            playing_grid[openY][openX + 1] = mines_secret_grid[openY][openX + 1]


    if openX > 0 and openY > 0 and playing_grid[openY - 1][openX - 1] == "#":
        if mines_secret_grid[openY - 1][openX - 1] == 0:
            new_points.append([openX - 1, openY - 1])
        elif mines_secret_grid[openY - 1][openX - 1] != "M":
            playing_grid[openY - 1][openX - 1] = mines_secret_grid[openY - 1][openX - 1]

    if openX < game_size - 1 and openY > 0 and playing_grid[openY - 1][openX + 1] == "#":
        if mines_secret_grid[openY - 1][openX + 1] == 0:
            new_points.append([openX + 1, openY - 1])
        elif mines_secret_grid[openY - 1][openX + 1] != "M":
            playing_grid[openY - 1][openX + 1] = mines_secret_grid[openY - 1][openX + 1]

    if openX > 0 and openY < game_size - 1 and playing_grid[openY + 1][openX - 1] == "#":
        if mines_secret_grid[openY + 1][openX - 1] == 0:
            new_points.append([openX - 1, openY + 1])
        elif mines_secret_grid[openY + 1][openX - 1] != "M":
            playing_grid[openY + 1][openX - 1] = mines_secret_grid[openY + 1][openX - 1]

    if openX < game_size - 1 and openY < game_size - 1 and playing_grid[openY + 1][openX + 1] == "#":
        if mines_secret_grid[openY + 1][openX + 1] == 0:
            new_points.append([openX + 1, openY + 1])
        elif mines_secret_grid[openY + 1][openX + 1] != "M":
            playing_grid[openY + 1][openX + 1] = mines_secret_grid[openY + 1][openX + 1]


    for i in new_points:
        self_and_around_opener(i[0], i[1])


screen_size = 775
game_size = 40
space_relation = 1/20
mines = int(game_size * (game_size/6))
square_size = ((1/space_relation)*screen_size) / (1 + (1/space_relation + 1)*game_size)
mines_secret_grid = [["#" for _ in range(game_size)] for _ in range(game_size)]
playing_grid = [["#" for _ in range(game_size)] for _ in range(game_size)]
mouse_squareX = 0
mouse_squareY = 0
game_over = False
clickable = True
counter = 0
max_counter = 0

closed_square_color = (128,128,128)
selected_square_color = (191,191,191)
mines_color = (209, 0, 0)
open_square_color = (255, 255, 255)
number1_color = (0, 0, 209)
number2_color = (0, 209, 0)
number3_color = (209, 0, 0)
number4_color = (163, 0, 163)
number5_color = (163, 163, 0)
number6_color = (0, 163, 163)

game_grid_prep()
drawer(mines_secret_grid)

pygame.init()

screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Minesweeper")
pygame.display.set_icon(pygame.image.load("Logo.png"))

running = True
mouse_pos = pygame.mouse.get_pos()
game_drawer(True)
GameStarted = False
while running:
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_BACKSPACE]:
            GameStarted = True
        if not game_over:
            game_drawer()

    if (GameStarted):
        if mouse_pressed[0]:
            if playing_grid[mouse_squareY][mouse_squareX] == "#":
                clicker()
            elif playing_grid[mouse_squareY][mouse_squareX] != "0" and clickable == True:
                clicker(False)
            clickable = False

        elif mouse_pressed[2] and playing_grid[mouse_squareY][mouse_squareX] == "#":
            playing_grid[mouse_squareY][mouse_squareX] = "M"
        elif not game_over:
            clickable = True
            if counter == max_counter:
                try:
                    mouse_squareX, mouse_squareY, left_click, state = solve(playing_grid, game_size)
                    if left_click:
                        clicker(state)
                    else:
                        playing_grid[mouse_squareY][mouse_squareX] = "M"
                    counter = 0
                    game_drawer()
                except:
                    game_over = True
                    print("Error")
            else:
                counter += 1

        if not game_over:
            game_over = True
            for i in playing_grid:
                for e in i:
                    if e == "#":
                        game_over = False
            if game_over:
                print("You Won!!")

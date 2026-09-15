import random


def no_free_spaces(grid:list):
    for i in grid:
        for e in i:
            if e != "#":
                return False

    return True

def around_counter(grid:int, x:int, y:int, letter):
    num = 0
    pos = []
    for i in range(y - 1, y + 2):
        for e in range(x - 1, x + 2):
            if i >= 0 and e >= 0:
                try:
                    if grid[i][e] == letter:
                        num += 1
                        pos.append([i, e])
                except:
                    pass
    return num, pos

def solve(grid, game_size):
    if no_free_spaces(grid):
        return random.randint(0, game_size - 1), random.randint(0, game_size - 1), True, True
    else:
        for i in range(game_size):
            for e in range(game_size):
                active_letter = grid[i][e]
                if active_letter not in ["#", "M", 0] or around_counter(grid, e, i, "#") != 0:
                    amount, positions = around_counter(grid, e, i, "#")
                    amount2 = around_counter(grid, e, i, "M")[0]
                    if amount + amount2 == active_letter and amount != 0:
                        if positions:
                            return positions[0][1], positions[0][0], False, True
                    if amount2 == active_letter and amount > 0:
                        return e, i, True, False

    while True:
        randomX = random.randint(0, game_size - 1)
        randomY = random.randint(0, game_size - 1)
        if grid[randomY][randomX] == "#":
            return randomX, randomY, True, True

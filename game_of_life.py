import random, time, os, copy

#const
WIDTH = 50
HEIGHT = 25
ALIVE = 'O'
DEAD = ' '

clear = lambda: os.system('cls')

def CountNeighbor(list, x, y):
    counter = 0
    left = (x - 1) % WIDTH
    right = (x + 1) % WIDTH
    up = (y - 1) % HEIGHT
    down = (y + 1) % HEIGHT

    if list[(left, up)]  == ALIVE:
        counter += 1
    if list[(left, y)]  == ALIVE:
        counter += 1
    if list[(left, down)]  == ALIVE:
        counter += 1
    if list[(x, up)]  == ALIVE:
        counter += 1
    if list[(x, down)]  == ALIVE:
        counter += 1
    if list[(right, down)]  == ALIVE:
        counter += 1
    if list[(right, y)]  == ALIVE:
        counter += 1
    if list[(right, up)]  == ALIVE:
        counter += 1

    return counter

nextCells = {}

#lot dakoty
'''for y in range(HEIGHT):
    for x in range(WIDTH):
        if (x == 0 and y == 0) or (x == 1 and y == 0) or (x == 2 and y == 0) or (x == 0 and y == 1) or (x == 1 and y == 2):
            nextCells[(x, y)] = ALIVE

        elif (x == 10 and y == 10) or (x == 11 and y == 10) or (x == 12 and y == 10) or (x == 10 and y == 11) or (x == 11 and y == 12):
            nextCells[(x, y)] = ALIVE

        else:
            nextCells[(x, y)] = DEAD'''


for y in range(HEIGHT):
    for x in range(WIDTH):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = DEAD
        else:
            nextCells[(x, y)] = ALIVE

while True:
    no_neighbor = 0
    oldCells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if oldCells[(x, y)] == ALIVE and (CountNeighbor(oldCells, x, y) == 2 or CountNeighbor(oldCells, x, y) == 3):
                nextCells[(x, y)] = ALIVE

            elif oldCells[(x, y)] == DEAD and CountNeighbor(oldCells, x, y) == 3:
                nextCells[(x, y)] = ALIVE

            else:
                nextCells[(x, y)] = DEAD


    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(nextCells[(x, y)], end='')

        print('')

    time.sleep(0.1)
    clear()

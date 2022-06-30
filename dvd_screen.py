# This is simple animation in cmd. It pretend DVD screensaver.

import sys, random, time

try:
    import bext

except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

WIDTH, HEIGHT = bext.size()
WIDTH -= 1
try:
    NUMBER_OF_LOGO = int(input('How many logos of DVD? '))
except TypeError:
    print('It must be an int.')
    sys.exit()

PAUSE = 0.035
COLORS = ['red', 'green', 'yellow', 'cyan']

RIGHT_UP = 'ru'
RIGHT_DOWN = 'rd'
LEFT_UP = 'lu'
LEFT_DOWN = 'ld'
DIRECTIONS = (RIGHT_UP, RIGHT_DOWN, LEFT_UP, LEFT_DOWN)

#names of key directory logos
DIR = 'direction'
X = 'x'
Y = 'y'
COLOR = 'color'

def main():
    bext.clear()

    logos = []
    for i in range(NUMBER_OF_LOGO):
        logos.append({COLOR: random.choice(COLORS),
                     X: random.randint(1, WIDTH - 4),
                     Y: random.randint(1, HEIGHT - 4),
                     DIR: random.choice(DIRECTIONS)})

        #make sure that value of X is even
        if logos[-1][X] %2 == 1:
            logos[-1][X] -= 1

    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('   ', end='')

            #if for corners (changing direction)
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = RIGHT_DOWN

            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = LEFT_DOWN

            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = RIGHT_UP

            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = LEFT_UP

            #if for edges (1. left, 2. up, 3. right, 4. down)
            #LEFT
            elif logo[X] == 0 and logo[DIR] == LEFT_UP:
                logo[DIR] = RIGHT_UP

            elif logo[X] == 0 and logo[DIR] == LEFT_DOWN:
                logo[DIR] = RIGHT_DOWN

            #UP
            elif logo[Y] == 0 and logo[DIR] == LEFT_UP:
                logo[DIR] = LEFT_DOWN

            elif logo[Y] == 0 and logo[DIR] == RIGHT_UP:
                logo[DIR] = RIGHT_DOWN

            #RIGHT
            elif logo[X] == WIDTH - 3 and logo[DIR] == RIGHT_UP:
                logo[DIR] = LEFT_UP

            elif logo[X] == WIDTH - 3 and logo[DIR] == RIGHT_DOWN:
                logo[DIR] = LEFT_DOWN

            #DOWN
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == LEFT_DOWN:
                logo[DIR] = LEFT_UP

            elif logo[Y] == HEIGHT - 1 and logo[DIR] == RIGHT_DOWN:
                logo[DIR] = RIGHT_UP

            #new values of coordiantes (X, Y)
            if logo[DIR] == LEFT_UP:
                logo[X] -= 2
                logo[Y] -= 1

            elif logo[DIR] == LEFT_DOWN:
                logo[X] -= 2
                logo[Y] += 1

            elif logo[DIR] == RIGHT_UP:
                logo[X] += 2
                logo[Y] -= 1

            elif logo[DIR] == RIGHT_DOWN:
                logo[X] += 2
                logo[Y] += 1

        for logo in logos:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')


        bext.goto(0, 0)
        sys.stdout.flush()
        time.sleep(PAUSE)
        #bext.clear()

if __name__ == '__main__':
    main()

import random, time

try:
    import bext
except ImportError:
    print('Please install bext from pip')

input('Press ENTER to start exploring a tunnel! ')

WIDTH = bext.width()
COLORS = ['red', 'green', 'blue', 'purple', 'cyan', 'yellow']
color = 'yellow'

tunnel_width = 15
behind_tunnel = int(WIDTH/2)
after_tunnel = WIDTH - tunnel_width - behind_tunnel

#main loop
while True:

    color = random.choice(COLORS)
    bext.fg(color)
    
    if len(COLORS) > 1:
        COLORS.remove(color)
    else:
        COLORS = ['red', 'green', 'blue', 'purple', 'cyan', 'yellow']

    print(behind_tunnel * '#' + tunnel_width * ' ' + after_tunnel * '#', end='')
    time.sleep(0.05)

    direction = random.choice((1, 2, 3, 4, 5, 6, 7))

    if direction in [1, 2, 3] and behind_tunnel > 3:
        behind_tunnel -= 1
        after_tunnel = WIDTH - tunnel_width - behind_tunnel

    elif direction in [5, 6, 7] and after_tunnel > 3:
        behind_tunnel += 1
        after_tunnel = WIDTH - tunnel_width - behind_tunnel

    else:
        pass
    

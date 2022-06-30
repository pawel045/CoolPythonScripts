# This script finds path for chess knight. He has to touch every field on board. 
# The script uses back-tracking algorithm to solve a problem.

def solver(board, n, pos, num_pos, move_x, move_y):

    if num_pos == (n**2):
        return True

    for i in range(8):
        (x_last, y_last) = (pos[0], pos[1])
        (x_now, y_now) = ((pos[0] + move_x[i]), (pos[1] + move_y[i]))

        if can_do(board, x_now, y_now, n):

            pos = (x_now, y_now)
            board[x_now][y_now] = num_pos
            num_pos += 1

            if solver(board, n, pos, num_pos, move_x, move_y):
                return True

            num_pos -= 1
            board[x_now][y_now] = -1
            pos = (x_last, y_last)

    return False

def can_do(board, x, y, n):

    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False

def print_board(b):
    for i in range(len(b[0])):
        for j in range(len(b[0])):
            if b[i][j] > 9 or b[i][j] < 0:
                print(f'{b[i][j]}', end = '| ')
            else:
                print(f' {b[i][j]}', end = '| ')
        print('')

def KT(n):
    # all position in board = -1
    board = [[-1 for i in range(n)] for j in range(n)]

    # [i][i] -> possibiities of knight move
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # firts value = 0
    board[0][0] = 0

    # coord first pos
    pos = (0, 0)

    # in every step knight print num_pos += 1
    num_pos = 1

    solver(board, n, pos, num_pos, move_x, move_y)

    if any(-1 in sublist for sublist in board):
        print('Solution doesn\'t exist')
        input()

    else:
        print("Solution:")
        print_board(board)
        input()

if __name__ == '__main__':
    KT(int(input('Enter a board dimension (np. 8): ')))

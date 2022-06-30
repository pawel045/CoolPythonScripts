board = [
    [0,0,0,0,4,0,2,0,0],
    [0,0,0,0,2,0,5,0,1],
    [0,6,0,0,0,0,7,0,0],
    [3,0,0,0,7,0,0,0,0],
    [0,0,5,0,0,2,3,0,0],
    [0,0,0,0,0,8,0,0,9],
    [0,7,0,0,0,3,0,0,8],
    [1,0,9,6,0,0,0,0,0],
    [0,0,6,0,0,0,0,1,0]
]

def solve(bo):
    find = find_empty(bo)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo, num, pos):
    #sprawdzenie wiersza
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #sprawdzenie kolumny
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #sprawdzenie kwadratu
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def print_board(bo):

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            print(str(bo[i][j]) + ' ', end='')
            if (j+1) % 3 == 0 and j != (len(bo[0]) - 1):
                print('| ', end='')
        if (i+1) % 3 == 0 and i != (len(bo) - 1):
            print('\n- - - - - - - - - - - ')
        else:
            print('')

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None


print_board(board)
solve(board)
print('XXXXXXXXXXXXXXXXXXXXX')
print_board(board)
input()

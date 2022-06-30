import os, time
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

haslo = str(input('Podaj haslo: ')).lower()
clearConsole()

def drawHangman(s):
    # drawing hangman, when s = 6 -> game over
    if s == 0:
        print(' ')

    if s == 1:
        print('___________')

    elif s == 2:
        print('\n'
              '    |\n'
              '    |\n'
              '    |\n'
              '    |\n'
              '____|____')

    elif s == 3:
        print('    ________\n'
              '    |\n'
              '    |\n'
              '    |\n'
              '    |\n'
              '____|____')

    elif s == 4:
        print('    ________\n'
              '    |      |\n'
              '    |      O\n'
              '    |\n'
              '    |\n'
              '____|____')

    elif s == 5:
        print('    ________\n'
              '    |      |\n'
              '    |      O\n'
              '    |     /|\ \n'
              '    |\n'
              '____|____')

    elif s == 6:
        print('    ________\n'
              '    |      |\n'
              '    |      O\n'
              '    |     /|\ \n'
              '    |     _|_\n'
              '____|____')

def numInPsw(string):
    # checinkg if the password is correct
    for letter in string:
        if letter.isdigit():
            return True

    return False

def seeBlanks(list):
    # display blanks and letters at the moment
    for pos in list:
        if pos == ' ':
            print('   ', end='')

        else:
            print(pos, end=' ')

def didWin(list):

    if '_' not in list:
        return True

    return False

def Hangman(haslo):
    # main part of game

    password = [let for let in haslo]
    blanks = []

    if numInPsw(haslo):
        print('Złe hasło!')
        quit()

    # add list to fill with password
    for letter in haslo:

        if letter == ' ':
            blanks.append(' ')
        else:
            blanks.append('_')

    shots = 0
    it_was = ['']

    while shots < 6:
        drawHangman(shots)
        print('\n')
        seeBlanks(blanks)
        print(f'\nLista użytych znaków: {it_was}')
        pick_let = str(input('\npodaj literkę: ')).lower()


        if pick_let in it_was:
            print('już była ta literka')
            time.sleep(1)
            clearConsole()

        elif pick_let.isdigit():
            print('to nie jest literka')
            time.sleep(1)
            clearConsole()

        elif len(pick_let) > 1:
            print('za dużo znaków')
            time.sleep(1)
            clearConsole()

        elif pick_let not in password:
            it_was.append(pick_let)
            shots += 1
            print('zle')
            time.sleep(1)
            clearConsole()

        else:
            it_was.append(pick_let)
            for let in range(len(password)):
                if pick_let == password[let]:
                    blanks[let] = password[let]
                continue

            clearConsole()

        if didWin(blanks):
            drawHangman(shots)
            print('\n')
            seeBlanks(blanks)
            print('\n\nWygrałeś!!')
            input()
            quit()


    drawHangman(shots)
    print('\n')
    seeBlanks(blanks)
    print(f'\nPrzegrałeś :( Hasło to {haslo.upper()}')
    input()

Hangman(haslo)

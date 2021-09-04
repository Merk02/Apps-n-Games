print('\n--- TicTacToe ---\n')

from random import randint

def board():
    print('\n',b[7],'|',b[8],'|',b[9])
    print('---+---+---')
    print('',b[4],'|',b[5],'|',b[6])
    print('---+---+---')
    print('',b[1],'|',b[2],'|',b[3],'\n')


b={1:' ',2:' ',3:' ',
   4:' ',5:' ',6:' ',
   7:' ',8:' ',9:' '}

def on():
    try:
        oi=int(input('play vs com (1)\nplay vs another person (2)\n'))
    except ValueError:
        print('\n3 attempts\nPlease enter a digit [1 or 2]\n')
        try:
            oi=int(input('play vs com (1)\nplay vs another person (2)\n'))
        except ValueError:
            print('\n2 attempts\nPlease enter a digit [1 or 2]\n')
            try:
                oi=int(input('play vs com (1)\nplay vs another person (2)\n'))
            except ValueError:
                print('\LAST CHANCE\nPlease enter a digit [1 or 2]\n')
                try:
                    oi=int(input('play vs com (1)\nplay vs another person (2)\n'))
                except ValueError:
                    print('\nWell\nGoodbye\n')
                    quit()
    if oi==1:
        board()
        com()
    elif oi==2:
        board()
        movex()
    else:
        print('\nPlease enter a digit [1 or 2]\n')
        on()
        

def restart():
    b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8],b[9]=' ',' ',' ',' ',' ',' ',' ',' ',' '
    board()
    on()
    

def end():
    r=input('\nStart new game? (y/n)\n')
    r=r.lower()
    if r==int:
        print('\nPlease enter y or n\n')
        start()
    if r=='y':
        restart()
    elif r!='y' and r!='n':
        print('\nPlease enter y or n\n')
        start()
    elif r=='n':
        print('\nGoodbye\n')
        quit()



# < SECTION HUMAN VS COM ---------------------------------------------

def com():
    xo=input('\nSelect X or O: ')
    if xo=='x' or xo=='X':
        turnx()
    elif xo=='o' or xo=='O':
        turno()
    elif xo==int:
        print('\nPlease enter X or O\n')
        com()
    else:
        print(f'\n\'{xo}\' is an invalid choice.\nPlease enter X or O\n')
        com()
    
def comx():
    cx=randint(1,9)
    if b[cx]==' ':
        b[cx]='X'
    elif b[cx]!=' ':
        comx()
    board()
    if b[1]==b[2]==b[3]=='X' or b[4]==b[5]==b[6]=='X' or b[7]==b[8]==b[9]=='X' or b[1]==b[4]==b[7]=='X' or b[2]==b[5]==b[8]=='X' or b[3]==b[6]==b[9]=='X' or b[1]==b[5]==b[9]=='X' or b[3]==b[5]==b[7]=='X':
        board()
        print('\nGame over.\ncomputer won\n')
        end()
    elif ' ' not in b.values():
        print('\nNo one won.\nTie\n')
        end()
    else:
        humano()

def turnx():
    tx=randint(1,2)
    if tx==1:
        como()
    else:
        humanx()

def turno():
    to=randint(1,2)
    if to==1:
        comx()
    else:
        humano()
    
def como():
    co=randint(1,9)
    if b[co]==' ':
        b[co]='O'
    elif b[co]!=' ':
        como()
    board()
    if b[1]==b[2]==b[3]=='O' or b[4]==b[5]==b[6]=='O' or b[7]==b[8]==b[9]=='O' or b[1]==b[4]==b[7]=='O' or b[2]==b[5]==b[8]=='O' or b[3]==b[6]==b[9]=='O' or b[1]==b[5]==b[9]=='O' or b[3]==b[5]==b[7]=='O':
        board()
        print('\nGame over.\nComputer won\n')
        end()
    elif ' ' not in b.values():
        print('\nNo one won.\nTie\n')
        end()
    else:
        humanx()

def humanx():
    try:
        hx=int(input('Input X: '))
    except ValueError:
        print('\n3 attempts\nPlease enter a digit [1-9]\n')
        try:
            hx=int(input('Input X: '))
        except ValueError:
            print('\n2 attempts\nPlease enter a digit [1-9]\n')
            try:
                hx=int(input('Input X: '))
            except ValueError:
                print('\LAST CHANCE\nPlease enter a digit [1-9]\n')
                try:
                    hx=int(input('Input X: '))
                except ValueError:
                    print('\nWell\nGoodbye\n')
                    quit()
    if hx in [1,2,3,4,5,6,7,8,9]:
        if b[hx]==' ':
            b[hx]='X'
            board()
        elif b[hx]!=' ':
            print('\nThis slot is occupied.\nChoose another slot\n')
            humanx()
        else:
            print('\nPlease enter a digit [1-9]\n')
            humanx()
    else:
        print('\nPlease enter a digit [1-9]\n')
        humanx()
    board()
    if b[1]==b[2]==b[3]=='X' or b[4]==b[5]==b[6]=='X' or b[7]==b[8]==b[9]=='X' or b[1]==b[4]==b[7]=='X' or b[2]==b[5]==b[8]=='X' or b[3]==b[6]==b[9]=='X' or b[1]==b[5]==b[9]=='X' or b[3]==b[5]==b[7]=='X':
        board()
        print('\nGame over.\nYou won\n')
        end()
    elif ' ' not in b.values():
        print('\nNo one won.\nTie\n')
        end()
    else:
        como()

def humano():
    try:
        ho=int(input('Input O: '))
    except ValueError:
        print('\n3 attempts\nPlease enter a digit [1-9]\n')
        try:
            ho=int(input('Input O: '))
        except ValueError:
            print('\n2 attempts\nPlease enter a digit [1-9]\n')
            try:
                ho=int(input('Input O: '))
            except ValueError:
                print('\LAST CHANCE\nPlease enter a digit [1-9]\n')
                try:
                    ho=int(input('Input O: '))
                except ValueError:
                    print('\nWell\nGoodbye\n')
                    quit()
    if ho in [1,2,3,4,5,6,7,8,9]:
        if b[ho]==' ':
            b[ho]='O'
        elif b[ho]!=' ':
            print('\nThis slot is occupied.\nChoose another slot\n')
            humano()
        else:
            print('\nPlease enter a digit [1-9]\n')
    else:
        print('\nPlease enter a digit [1-9]\n')
        humano()
    board()
    if b[1]==b[2]==b[3]=='O' or b[4]==b[5]==b[6]=='O' or b[7]==b[8]==b[9]=='O' or b[1]==b[4]==b[7]=='O' or b[2]==b[5]==b[8]=='O' or b[3]==b[6]==b[9]=='O' or b[1]==b[5]==b[9]=='O' or b[3]==b[5]==b[7]=='O':
        board()
        print('\nGame over.\nYou won\n')
        end()
    elif ' ' not in b.values():
        print('\nNo one won.\nTie\n')
        end()
    else:
        comx()    

# END SECTION HUMAN VS COM /> -----------------------------------------------



# < SECTION HUMAN VS HUMAN ---------------------------------------------------
    
def movex():
    try:
        x=int(input('Input X: '))
    except ValueError:
        print('\n3 attempts\nPlease enter a digit [1-9]\n')
        try:
            x=int(input('Input X: '))
        except ValueError:
            print('\n2 attempts\nPlease enter a digit [1-9]\n')
            try:
                x=int(input('Input X: '))
            except ValueError:
                print('\LAST CHANCE\nPlease enter a digit [1-9]\n')
                try:
                    x=int(input('Input X: '))
                except ValueError:
                    print('\nWell\nGoodbye\n')
                    quit()
    if x in [1,2,3,4,5,6,7,8,9]:
        if b[x]==' ':
            b[x]='X'
        elif b[x]!=' ':
            print('\nThis slot is occupied.\nChoose another slot\n')
            movex()
        else:
            print('\nPlease enter a digit [1-9]\n')
    else:
        print('\nPlease enter a digit [1-9]\n')
        movex()
    board()
    if b[1]==b[2]==b[3]=='X' or b[4]==b[5]==b[6]=='X' or b[7]==b[8]==b[9]=='X' or b[1]==b[4]==b[7]=='X' or b[2]==b[5]==b[8]=='X' or b[3]==b[6]==b[9]=='X' or b[1]==b[5]==b[9]=='X' or b[3]==b[5]==b[7]=='X':
        board()
        print('\nGame over.\nx won\n')
        end()
    elif ' ' not in b.values():
        print('\nNo one won.\nTie\n')
        end()
    else:
        moveo()
    

def moveo():
    try:
        o=int(input('Input O: '))
    except ValueError:
        print('\n3 attempts\nPlease enter a digit [1-9]\n')
        try:
            o=int(input('Input O: '))
        except ValueError:
            print('\n2 attempts\nPlease enter a digit [1-9]\n')
            try:
                o=int(input('Input O: '))
            except ValueError:
                print('\LAST CHANCE\nPlease enter a digit [1-9]\n')
                try:
                    o=int(input('Input O: '))
                except ValueError:
                    print('\nVery Well\nGoodbye\n')
                    quit()
    if o in [1,2,3,4,5,6,7,8,9]:
        if b[o]==' ':
            b[o]='O'
        else:
            print('\nThis slot is occupied.\nChoose another slot\n')
            moveo()
    else:
        print('\nPlease enter a digit [1-9]\n')
        moveo()
    board()
    if b[1]==b[2]==b[3]=='O' or b[4]==b[5]==b[6]=='O' or b[7]==b[8]==b[9]=='O' or b[1]==b[4]==b[7]=='O' or b[2]==b[5]==b[8]=='O' or b[3]==b[6]==b[9]=='O' or b[1]==b[5]==b[9]=='O' or b[3]==b[5]==b[7]=='O':
        board()
        print('\nGame over.\no won\n')
        end()
    elif ' ' not in b.values():
        print('\nNo one won.\n Tie\n')
        end()
    else:
        movex()

# END SECTION HUMAN VS HUMAN /> -----------------------------------------


on()

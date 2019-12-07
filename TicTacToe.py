board = ['_1_','_2_','_3_','_4_','_5_','_6_','_7_','_8_','_9_']

def p1wins():
    print('Player X wins the game')
    response = input ('Do you want to replay the game?\nTo replay press r and then enter: ')
    if response == 'r':
        for i in range (0,9):
            board[i] = '_'+str(i+1)+'_'
        playgame()
    else:
        exit()

def p2wins():
    print('Player O wins the game')
    response = input ('Do you want to replay the game?\nTo replay press r and then enter: ')
    if response == 'r':
        for i in range (0,9):
            board[i] = '_'+str(i+1)+'_'
        playgame()
    else:
        exit()


def tie():
    print('Game is tie')
    response = input ('Do you want to replay the game?\nTo replay press r and then enter: ')
    if response == 'r':
        for i in range (0,9):
            board[i] = '_'+str(i+1)+'_'
        playgame()
    else:
        exit()
    

def checkwin():
    for i in [0,1,2]:
        if ((board[i] == board[i+3]) and (board[i] == board[i+6])):
            if board[i] == ' X ':
                p1wins()
            else :
                p2wins()
        else:
            pass
    for i in [0,3,6]:
        if ((board[i] == board[i+1]) and (board[i] == board[i+2])):
            if board[i] == ' X ':
                p1wins()
            else :
                p2wins()
        else:
            pass
    for i in [0]:
        if ((board[i]==board[i+4]) and (board[i]==board[i+8])):
            if board[i] == ' X ':
                p1wins()
            else :
                p2wins()
        else:
            pass
    for i in [2]:
        if ((board[i]==board[i+2]) and (board[i]==board[i+4])):
            if board[i] == ' X ':
                p1wins()
            else :
                p2wins()
        else:
            pass

def checktie():
        r1 = (board[0] == ('_1_'))
        r2 = (board[1] == ('_2_'))
        r3 = (board[2] == ('_3_'))
        r4 = (board[3] == ('_4_'))
        r5 = (board[4] == ('_5_'))
        r6 = (board[5] == ('_6_'))
        r7 = (board[6] == ('_7_'))
        r8 = (board[7] == ('_8_'))
        r9 = (board[8] == ('_9_'))

        if ( r1 or r2 or r3 or r4 or r5 or r6 or r7 or r8 or r9) is False:
            tie()
        else:
            pass



def inputposition():
    position = int(input('choose position to change: ')) - 1
    return position
        

def playgame():
    print('Tic-tac-toe is a game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.')
    boarddisplay()
    handleturnp1()


def boarddisplay():
    print (board[0] + ' | ' + board[1] + ' | ' + board[2])
    print ('--' + '--' + '+-' +  '--' + '-+' + '--' + '---')
    print (board[3] + ' | ' + board[4] + ' | ' + board[5])
    print ('--' + '--' + '+-' +  '--' + '-+' + '--' + '---')
    print (board[6] + ' | ' + board[7] + ' | ' + board[8])


def handleturnp1():
    board[inputposition()] = ' X '
    boarddisplay()    
    checkwin()
    checktie()
    handleturnp2()


def handleturnp2():
    board[inputposition()] = ' O '
    boarddisplay()    
    checkwin()
    checktie()
    handleturnp1()



playgame()
    

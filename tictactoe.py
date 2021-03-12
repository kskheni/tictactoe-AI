import math

def show_board(board):
    print("")

    for i in range(3):
        print("",board[i][0],"|",board[i][1],"|",board[i][2])
        if i<2:
            print("~~~~~~~~~~~")

def empty(board):
    emt=[]

    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                emt.append(i*10+j)

    return emt

def isWinner(board,player):
    #same column
    for i in range(3):
        if board[i][0]==player:
            if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
                return True

    #same row
    for i in range(3):
        if board[0][i]==player:
            if board[0][i]==board[1][i] and board[1][i]==board[2][i]:
                return True
    
    #diagonal
    if board[1][1]==player:
        if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
            return True
        if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
            return True  

    return False

def isGameOver(board):
    if isWinner(board,'O'):
        return 'Owin'
    
    if isWinner(board,'X'):
        return 'Xwin'

    depth=len(empty(board))
    if depth==0:
        return 'Draw'

    return '0'

def eval(board):
    if isWinner(board,'X'):
        return 1
    elif isWinner(board,'O'):
        return -1
    else:
        return 0

def human_Turn(board):
    temp=int(input("\nEnter number according to the move you want to make(1,2,...,9)"))

    while((temp>9 or temp<1) or board[(temp-1)//3][(temp-1)%3]!=' '):
        if temp>9 or temp<1:
            temp=int(input("Inappropriate input!! enter new the number."))
        else:
            temp=int(input("Spot already filled!! Enter new the number."))

    board[(temp-1)//3][(temp-1)%3]='O'

def alpha_beta_pruning(board, alpha, beta, isMax):
    if isGameOver(board)!='0':
        return (eval(board),0,0)

    emt=empty(board)

    if isMax:
        val=-math.inf

        for x in emt:
            board[x//10][x%10]='X'

            # val=max(val,alphabeta(board, alpha, beta, False))
            (curVal,minI,minJ) = alpha_beta_pruning(board, alpha, beta, False)
            if val<curVal:
                val=curVal
                chosenI=x//10
                chosenJ=x%10

            board[x//10][x%10]=' '
            
            alpha=max(alpha,val)

            if alpha >= beta:
                break
        
        return (val,chosenI,chosenJ)

    else:
        val=math.inf

        for x in emt:
            board[x//10][x%10]='O'

            # val=min(val,alphabeta(board, alpha, beta, True))
            (curValmin,maxI,maxJ)=alpha_beta_pruning(board, alpha, beta, True)
            if val>curValmin:
                val=curValmin
                chosenI=x//10
                chosenJ=x%10

            board[x//10][x%10]=' '

            beta=min(beta,val)

            if alpha >= beta:
                break
        
        return (val,chosenI,chosenJ)

def tictactoe():
    board=[ [' ',' ',' '], [' ',' ',' '], [' ',' ',' '] ]

    temp=[ [1,2,3], [4,5,6] , [7,8,9] ]
    show_board(temp)    
    print("\nEnter appropriate number to make a move when it's your turn\n\nYou: O\nComputer: X")

    human_Turn(board)
    show_board(board)

    while isGameOver(board)=='0':
        print("\nAI's Turn:")
        (val,i,j) = alpha_beta_pruning(board, -math.inf, math.inf, True)
        board[i][j]='X'
        show_board(board)

        if isGameOver(board)!='0':
            break

        human_Turn(board)
        show_board(board)

    if isGameOver(board)=="Owin":
        print("\n\nYou won\n")
    elif isGameOver(board)=="Xwin":
        print("\n\nAI won\n")
    elif isGameOver(board)=="Draw":
        print("\n\nIt's a Draw")

    input("\nPress enter to exit!!\n")

if __name__=='__main__':
    tictactoe()

#Gane Requires 2 players 

import pprint
board={'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
#pprint.pprint(board) Debugging Dic values

def printboard(board):                                      #fuc to display the board
    print(' '+board['1']+" | "+board['2']+" | "+board['3'])
    print("---+---+---")
    print(' '+board['4']+" | "+board['5']+" | "+board['6'])
    print("---+---+---")
    print(' '+board['7']+" | "+board['8']+" | "+board['9'])
    
def checkboard(board):                              #checking the status of board
    if(board['1']==board['2']==board['3']=='O' or board['1']==board['2']==board['3']=='X'):   # returns X or O if one wins 
        return (str(board['2']))
                
    if(board['4']==board['5']==board['6']=='X' or board['4']==board['5']==board['6']=='O'):
        return (str(board['5']))
                
    if(board['7']==board['8']==board['9']=='X' or board['7']==board['8']==board['9']=='O'):
        return (str(board['8']))
                   
    if(board['1']==board['4']==board['7']=='X' or board['1']==board['4']==board['7']=='O'):
        return (str(board['4']))
                   
    if(board['2']==board['5']==board['8']=='X' or board['2']==board['5']==board['8']=='O'):
        return (str(board['5']))
                   
    if(board['3']==board['6']==board['9']=='X' or board['3']==board['6']==board['9']=='O'):
        return (str(board['6']))
                   
    if(board['1']==board['5']==board['9']=='X' or board['1']==board['5']==board['9']=='O'):
        return (str(board['5']))
                   
    if(board['3']==board['5']==board['7']=='X' or board['3']==board['5']==board['7']=='O'):   
        return (str(board['5']))
    
    else:
        return (0)                  #if playable moves exits Return 0

def playermove(playermarker,board):            #function call for each player move
    print("Enter Cell Number:")
    cellnum=input()
    board[cellnum]=playermarker
     
print('Player 1, "X" or "O"? ')                 #player 1 goes first hence asking his mark
player1=input()
player1=player1.upper()

if(player1=='X'):                               #assigning player 2's marker depending on player 1
    print("Player 1 is X" +" Player 2 is : O")  
    player2='O'
elif(player1=='O'):
    print("Player 1 is O" +" Player 2 is : X")
    player2="X"
    
status=0            #status holds if the game should be continued or finished, default it is zero
i=1                 # i switches between 1 and 0, for each player's turn
printboard(board)
while (status==0):        #looping until status changes
    if(i==1):
        print(str(player1)+"'s  Turn")
        playermove(player1,board)
        i+=1                    #updating player's move so other one can play
        
    elif(i==0):
        print(str(player2)+"'s Turn")
        playermove(player2,board)
        i+=1
    
    i=i%2                   #complimenting player move
    
    printboard(board)
    status=checkboard(board)   
    
    if(status=='X'):        #This part describes the Results or incase of a draw
        print("X wins! Congratulations! ")
        break
    if(status=='O'):
        print("O wins! Congratulations! ")
        break
    draw='' in board.values()   #as long as null string exists, there are playable moves
    if(draw==False):
        print("Draw")
        status=-1
        break
         

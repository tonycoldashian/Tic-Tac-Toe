#attempt to make tic tac toe game with one player as computer itself

import random,pprint
board={'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
#pprint.pprint(board) Debugging Dic values

def printboard(board):                                      #fuc to display the board
    print(' '+board['1']+" | "+board['2']+" | "+board['3'])
    print("---+---+---")
    print(' '+board['4']+" | "+board['5']+" | "+board['6'])
    print("---+---+---")
    print(' '+board['7']+" | "+board['8']+" | "+board['9'])
    print(" ")
    
def checkboard(board):                              #checking the status of board
    if(board['1']==board['2']==board['3']=='X' or board['1']==board['2']==board['3']=='O'):   # returns X or O if one wins 
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
    print("Enter Cell Number:",end=' ')
    cellnum=input()
    if(board[cellnum]==''):
        board[cellnum]=playermarker
    else:
        print("Can't Place on Existing Cell")
        playermove(playermarker,board)
        
randomcell='1'
def computermove(playermarker,board):
    global randomcell,computer
    randomcell=random.randint(1,9)
    randomcell=str(randomcell)
    if(board[randomcell]==''):
        print("Entered Cell Number:"+randomcell)
        board[randomcell]=playermarker
        return

    else:
        computermove(computer,board)

print("\nWelcome Human\n")
print("--------------------")       #player 1 goes first hence asking his mark                                   
print('\nChoose, "X" or "O"? ') 
player1=input()
player1=player1.upper()
        
if(player1=='X'):                               #assigning player 2's marker depending on player 1
    print("\nHuman is X" +"||"+" Computer is : O")  
    computer='O'
elif(player1=='O'):
    print("\nHuman is O" +"||"+" Computer is : X")
    computer="X"
    
status=0            #status holds if the game should be continued or finished, default it is zero
i=1                 # i switches between 1 and 0, for each player's turn
printboard(board)
while (status==0):        #looping until status changes
    if(i==1):
        print(str(player1)+" || Human's  Turn :\n")
        playermove(player1,board)
        i+=1                    #updating player's move so other one can play
        
    elif(i==0):
        print(str(computer)+" || Computer's Turn:\n")
        computermove(computer,board)
        i+=1
    
    i=i%2   

    printboard(board)
    status=checkboard(board)   
    
    if(status=='X'):        #This part describes the Results or incase of a draw
        print("X wins! \n")     
        break
    if(status=='O'):
        print("O wins! \n")
        break
    draw='' in board.values()   #as long as null string exists, there are playable moves
    if(draw==False):
        print("Draw \n")
        status=-1
        break


# coding: utf-8

# In[17]:


import os
def clearoutput():
    os.system( 'cls' )


# In[23]:


def displayboard(board):
    
    clearoutput()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])



# In[24]:


def playerin():
    
    marker=''
    while not (marker=='X' or marker=='O'):
        marker=input('Player 1: Choose X or O').upper()
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')
    


# In[25]:


def markerplace(board, marker, position):
    board[position] =marker


# In[26]:


def checkwin(board,mark):
     return ((board[9] == mark and board[5] == mark and board[1] == mark) or #diag1
    (board[7] == mark and board[5] == mark and board[3] == mark) or #diag2
    (board[4] == mark and board[5] == mark and board[6] == mark) or #mid1
    (board[1] == mark and board[2] == mark and board[3] == mark) or #bot
    (board[7] == mark and board[4] == mark and board[1] == mark) or #downleft
    (board[8] == mark and board[5] == mark and board[2] == mark) or #mid3
    (board[9] == mark and board[6] == mark and board[3] == mark) or #downright
    (board[7] == mark and board[8] == mark and board[9] == mark)) #top
    


# In[27]:


import random
def choosefirst():
    if random.randint(0,1) ==0:
        return 'Player 1'
    else:
        return 'Player 2'


# In[28]:


def freespace(board, position):
    return board[position] == ' '


# In[29]:


def fullboard(board):
    for x in range(1,10):
        if freespace(board, x):
            return False
    return True


# In[30]:


def chooseplace(board):
    position=' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not freespace(board, int(position)):
        
        position=input('Choose a position 1-9:')
    return int(position)


# In[33]:



def replay():
    
    ans=input('Do you want to play again? Enter Yes or No: ').lower()
    if ans == 'Yes':
        return True
    else:
        return False


# In[34]:


print('Welcome to Tic-Tac-Toe!')

while True:
    theboard = [' '] * 10
    player1_marker, player2_marker = playerin()
    turn = choosefirst()
    print(turn + ' will go first.')
    game_on = True
    
    while game_on:
        if turn == 'Player 1':
            
            displayboard(theboard)
            position = chooseplace(theboard)
            markerplace(theboard, player1_marker, position)

            if checkwin(theboard, player1_marker):
                displayboard(theboard)
                print('Congratulations Player 1! You have won!')
                game_on = False
            else:
                if fullboard(theboard):
                    displayboard(theboard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'

        else:
          
            displayboard(theboard)
            position = chooseplace(theboard)
            markerplace(theboard, player2_marker, position)

            if checkwin(theboard, player2_marker):
                displayboard(theboard)
                print('Congratulations Player 2! You have won!')
                game_on = False
            else:
                if fullboard(theboard):
                    displayboard(theboard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


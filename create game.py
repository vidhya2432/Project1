import os
os.system("cls")
board = ["0","1","2",
         "3","4","5",
         "6","7","8"]
against_computer = True
def free_boxes():
    pass
def computer():
    pass
def game_over():
    result = True
    for box in board:
        if (box=="X" or box=="O"):
            continue
        else:
            result = False
            break
    return result
def display_board():
    os.system("cls")
    for i in range(len(board)):
        print(board[i],end=" ")
        if (i+1)%3==0:
            print()
    print()
def is_free(pos):
    if(board[pos] == "X" or board[pos] == "O"):
        return False
    else:
        return True
def take_turn(player):
    pos = int(input(player+" enter your pos:"))
    if(pos>=0 and pos<=8) and is_free(pos):
        board[pos] = player
        display_board()
    else:
        print("Wrong Selection")
        take_turn(player)
def occupancy(player):
    result = " "
    for i in range(len(board)):
        if(board[i]==player):
            result = result+str(i)
    return result
def check_win(player_occupancy):
    possible_wins = ["012","345","678","147","258","048","246"]
    for possible_wins in possible_wins:
        result = True
        for pos in possible_wins:
            if pos in player_occupancy:
                continue
            else:
                result = False

        if(result):
            return True
            break
        else:
            continue
    return False
def is_won(player):
    result = False
    print(player+" "+occupancy(player))
    if (check_win(occupancy(player))):
        result = True
    return result
display_board()
while(True):
    if (not game_over()):
        take_turn("X")
        if(is_won("X")):
            print("X is the winner")
            break
    else:
        break
    if (not game_over()):
        take_turn("O")
        if(is_won("O")):
            print("O is the winner")
            break
    else:
            break

print("Game Over")
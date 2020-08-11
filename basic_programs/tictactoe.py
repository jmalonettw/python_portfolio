def tictactoe():
    cross = '-----------'
    vert = '   |   |   '
    board = ["placeholder","1","2","3","4","5","6","7","8","9"]
    playerone = "NaN"
    playertwo = "NaN"
    playernum = 1
    playcount = 0
    win = False

    def place_mark():
        player_mark = input("Player {}: Which position would you like to choose?".format(str(playernum)))
        if player_mark != board[int(player_mark)]:
            print("Please choose an unchosen number from 1 to 9.")
        elif player_mark != board[int(player_mark)]:
            print("That slot has already been taken. Please choose another")
        else:
            if playernum == 1:
                board[int(player_mark)] = playerone
                playernum = 2
                playcount += 1
            else:
                board[int(player_mark)] = playertwo
                playernum = 1
                playcount += 1

    #place_mark()

    def win_condition():
        global win
        if (board[1] == board[2] == board[3]) or (board[4] == board[5] == board[6]) or (board[7] == board[8] == board[9])\
            or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]) or (board[3] == board[6] == board[9])\
            or (board[1] == board[5] == board[9]) or (board[3] == board[5] == board[7]):
            print("Cogratulations Player {}! You win!".format(playernum))
            win = True
        elif playcount == 9:
            print("Stalemate!")
            win = True
    win_condition()


    def print_board():
        print(vert)
        print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
        print(vert)
        print(cross)
        print(vert)
        print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
        print(vert)
        print(cross)
        print(vert)
        print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
        print(vert)
    #print_board()

    while playerone != "X" and  playerone != "O":
        playerone = input("Player 1: Would you like to be X's or O's?\n").upper()
        if playerone == "X":
             playertwo = "O"
        elif playerone == "O":
            playertwo = "X"
        elif playerone != "X" or playerone != "O":
            print('You need to choose either "X" or "O".')
    print_board()

    while win == False:
        place_mark()
        print_board()
        win_condition()

tictactoe()

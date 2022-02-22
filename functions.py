# Tic Tac Toe game
def game_ttt():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    print("Let's the game begin. \n")
    i = 0
    while True:
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
            player = "One"
            sign = "X"
        else:
            player = "Two"
            sign = "O"
        draw_board(game)
        lst_1 = check(game, i)
        num = result(lst_1)
        if num == 1:
            break
        print(game)
        if i == 9:
            break
        i += 1
        while True:
            while True:
                user_one = str(
                    input("Player " + player + " where You want to place '" + sign +
                          "'? (row,col) - accepted numbers from 1 to 3: \n"))
                if "," in user_one:
                    usr_cor = user_one.split(",")
                    usr_row = int(usr_cor[0].strip()) - 1
                    usr_col = int(usr_cor[1].strip()) - 1
                    if usr_col > 2 or usr_col < 0 or usr_row > 2 or usr_row < 0:
                        print("Your coordinates are out of range, please choose another")
                    else:
                        if game[usr_row][usr_col] == 0:
                            game[usr_row][usr_col] = sign
                            break
                        else:
                            print("This cell is non-available, please choose another")
                else:
                    print("Wrong coordinates format - try again")
            break


# Checking the game board for Tic Tac Toe
def check(game_1, y):
    lst = [0, 0]
    for i in range(3):
        for z in range(3):
            # row
            if game_1[i][0] == "X" and game_1[i][1] == "X" and game_1[i][2] == "X":
                lst = [1, 0]
                break
            # row
            elif game_1[i][0] == "O" and game_1[i][1] == "O" and game_1[i][2] == "O":
                lst = [0, 1]
                break
            # column
            elif game_1[0][i] == "X" and game_1[1][i] == "X" and game_1[2][i] == "X":
                lst = [1, 0]
                break
            # column
            elif game_1[0][i] == "O" and game_1[1][i] == "O" and game_1[2][i] == "O":
                lst = [0, 1]
                break
            # diagonals
            elif game_1[0][0] == game_1[1][1] == game_1[2][2] == "X" or game_1[0][2] == game_1[1][1] \
                    == game_1[2][0] == "X":
                lst = [1, 0]
                break
            elif game_1[0][0] == game_1[1][1] == game_1[2][2] == "O" or game_1[0][2] == game_1[1][1] \
                    == game_1[2][0] == "O":
                lst = [0, 1]
                break
            elif y == 9:
                lst = [1, 1]
                break
            else:
                break
    return lst


# Printing the result for Tic Tac Toe
def result(lst):
    if lst[0] == 1 and lst[1] == 0:
        print("Player One wins! \n Game Over!")
        return 1
    elif lst[0] == 0 and lst[1] == 1:
        print("Player Two wins \n Game Over!")
        return 1
    elif lst[0] == 1 and lst[1] == 1:
        print("It's a tie \n Game Over!")
        return 1
    else:
        print("Game On!")
    # print(lst)


# Draw a game board - my solution
def draw_board(game):
    x, y = 3, 3
    for i in range(1, x + 1, 1):
        # first row
        if i == 1:
            for z in range(1, y + 1, 1):
                if z < y:
                    print(" ---", end='')
                else:
                    print(" ---", end='\n')
            for v in range(1, y + 1, 1):
                if v == 1:
                    print("| " + str(game[i - 1][v - 1]) + " |", end='')
                elif v < y:
                    print(" " + str(game[i - 1][v - 1]) + " |", end='')
                else:
                    print(" " + str(game[i - 1][v - 1]) + " |", end='\n')
            for w in range(1, y + 1, 1):
                if w < y:
                    print(" ---", end='')
                else:
                    print(" ---", end='\n')
        else:
            # second and third row
            for v in range(1, y + 1, 1):
                if v == 1:
                    print("| " + str(game[i - 1][v - 1]) + " |", end='')
                elif v < y:
                    print(" " + str(game[i - 1][v - 1]) + " |", end='')
                else:
                    print(" " + str(game[i - 1][v - 1]) + " |", end='\n')
            for w in range(1, y + 1, 1):
                if w < y:
                    print(" ---", end='')
                else:
                    print(" ---", end='\n')

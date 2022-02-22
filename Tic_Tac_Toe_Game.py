import functions

while True:
    check = input("Do You want to play? (Y)es or (N)o")
    if check.lower() == "y":
        functions.game_ttt()
    else:
        break

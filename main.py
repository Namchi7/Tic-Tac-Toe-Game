def displayGrid(xState, zState):        # displayes the gird with xState and zstate values
    one = "X" if xState[0] else ("O" if zState[0] else 1)
    two = "X" if xState[1] else ("O" if zState[1] else 2)
    three = "X" if xState[2] else ("O" if zState[2] else 3)
    four = "X" if xState[3] else ("O" if zState[3] else 4)
    five = "X" if xState[4] else ("O" if zState[4] else 5)
    six = "X" if xState[5] else ("O" if zState[5] else 6)
    seven = "X" if xState[6] else ("O" if zState[6] else 7)
    eight = "X" if xState[7] else ("O" if zState[7] else 8)
    nine = "X" if xState[8] else ("O" if zState[8] else 9)

    print(f" {one} | {two} | {three} ")
    print(f"---|---|---")
    print(f" {four} | {five} | {six} ")
    print(f"---|---|---")
    print(f" {seven} | {eight} | {nine} ")


def checkWin(xState, zState):               # to check the winner
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        if((xState[win[0]] + xState[win[1]] + xState[win[2]]) == 3):
            print("X wins!")
            return 1

        if((zState[win[0]] + zState[win[1]] + zState[win[2]]) == 3):
            print("O wins!")
            return 0

    return -1


def start():                    # starting function
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    turn = 1  # 1 for X and 0 for O
    while(True):
        displayGrid(xState, zState)
        if turn == 1:
            print("X's turn")
            value = int(input("Please enter a value: "))
            xState[(value - 1)] = 1

        else:
            print("O's turn")
            value = int(input("Please enter a value: "))
            zState[(value - 1)] = 1

        cwin = checkWin(xState, zState)
        if(cwin != -1):
            print("Match Over")
            break

        turn = 1 - turn

    return 0


start()

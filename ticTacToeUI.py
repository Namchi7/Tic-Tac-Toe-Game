import tkinter as tk
from tkinter import DISABLED, messagebox


xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1  # 1 for X and 0 for O


def disableAllBtn():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def checkWin(xState, zState):               # to check the winner

    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        if((xState[win[0]] + xState[win[1]] + xState[win[2]]) == 3):
            messagebox.showinfo("Result", "X Wins!!!")
            disableAllBtn()
            return 1

        if((zState[win[0]] + zState[win[1]] + zState[win[2]]) == 3):
            messagebox.showinfo("Result", "O Wins!!!")
            disableAllBtn()
            return 0

    sum = 0

    for i in range(9):
        sum += (xState[i] + zState[i])

        if sum == 9:
            disableAllBtn()
            return -1


def b_click(b, value):
    global xState, zState, turn

    if turn == 1 and b["text"] == " ":
        b["text"] = "X"
        xState[(value - 1)] = 1
        b.config(state=DISABLED)

    else:
        b["text"] = "O"
        zState[(value - 1)] = 1
        b.config(state=DISABLED)

    cwin = checkWin(xState, zState)
    if(cwin == -1):
        messagebox.showinfo("Result", "Match Over!!! It is a TIE!!!")

    turn = 1 - turn

    return 0


root = tk.Tk()
root.title("Tic Tac Toe")


def cleanStart():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global xState, zState, turn
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O

    b1 = tk.Button(root, text=" ", font=(
        "Calibri", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: b_click(b1, 1))
    b2 = tk.Button(root, text=" ", font=(
        "Calibri", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: b_click(b2, 2))
    b3 = tk.Button(root, text=" ", font=(
        "Calibri", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: b_click(b3, 3))

    b4 = tk.Button(root, text=" ", font=(
        "Calibri", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: b_click(b4, 4))
    b5 = tk.Button(root, text=" ", font=(
        "Calibri", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: b_click(b5, 5))
    b6 = tk.Button(root, text=" ", font=(
        "Calibri", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: b_click(b6, 6))

    b7 = tk.Button(root, text=" ", font=(
        "Calibri", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: b_click(b7, 7))
    b8 = tk.Button(root, text=" ", font=(
        "Calibri", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: b_click(b8, 8))
    b9 = tk.Button(root, text=" ", font=(
        "Calibri", 20), height=3, width=8, bg="SystemButtonFace", command=lambda: b_click(b9, 9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    messagebox.showinfo("Start", "X starts first")


gameMenu = tk.Menu(root)
root.config(menu=gameMenu)

menuOptions = tk.Menu(gameMenu, tearoff=False)
gameMenu.add_cascade(label="Options", menu=menuOptions)
menuOptions.add_command(label="Reset Game", command=cleanStart)

cleanStart()

root.mainloop()

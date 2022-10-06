#collaborated with PickolZi

from tkinter import *
import tkinter.font as font

window = Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

#Creating list to store objects
button_positions = [[],
                    [],
                    []]

#Stores information about
positions =[["","",""],
            ["","",""],
            ["","",""]]

winner = False

#Resets the board and the stored information
def restart():
    global winner
    global move_number
    for i in range (3):
        for j in range (3):
            button_positions[i][j]["text"] = ""
            positions[i][j]=""
    winner = False
    move_number = 0
    next_turn["text"] = "It's X's turn."

def declare_winner():
    global winner
    global move_number
    if (move_number == 9):
        next_turn["text"]="It's a tie!"
    try:
        next_turn["text"] = (check_winner() + " is " + char + "!")
        winner = True
    except:
        pass

move_number=0
def edit_button (x,y):
    if winner:
        return
    #Check if button has text
    if (button_positions[x][y]["text"] != ""):
        return
    #Set button to "x" or "o"
    global move_number
    global char
    move_number += 1
    if (move_number % 2 == 0):
        char = "O"
        next_turn["text"] = "It's X's turn."
    else:
        char = "X"
        next_turn["text"]="It's O's turn."
    button_positions[x][y]["text"] = char
    positions[x][y] = char
    declare_winner()
   

#Views board to determine whether there is a winner
def check_winner():
    for i in range(3):
        if (positions[i][0] == positions[i][1] and positions[i][1] == positions[i][2] and positions[i][0]!=""):
            return "Winner"
        elif (positions[0][i] == positions[1][i] and positions[1][i] == positions[2][i] and positions[0][i]!=""):
            return "Winner"
        else:
            continue
    if (positions[0][0]==positions[1][1] and positions[1][1]==positions[2][2] and positions[1][1]!=""):
        return "Winner"
    elif (positions[0][2]==positions[1][1] and positions[1][1]==positions[2][0] and positions[1][1]!=""):
        return "Winner"

#Setting up buttons
for x in range(3):
    for y in range(3):
        button = Button(window, command=lambda a=x,b=y:edit_button(a,b), bg="#20bebe", fg="white",width=3)
        f=font.Font(family="Times New Roman", size=70)
        button["font"] = f
        button.grid(column=y, row=x+1)
        button_positions[x].append(button)

#Display information
next_turn = Label(window, text="It's X's turn.", anchor=CENTER)
next_turn.grid(column=0,row=0, columnspan=3)

#Restart Button
restart_btn = Button(window, height=2, width=5, command=restart)
restart_btn.grid(column=0, row=5, columnspan=3, pady=10, sticky=S)
restart_btn["text"] = "Restart"



window.mainloop()

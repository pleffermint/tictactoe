#collaborated with PickolZi

from tkinter import *
import tkinter.font as font

window = Tk()
window.title("Tic Tac Toe")

positions =[[],
            [],
            []]

#create buttons
for x in range(3):
    for y in range(3):
        button = Button(window, command=lambda a=x,b=y:edit_button(a,b), bg="#20bebe", fg="white",width=3)
        f=font.Font(family="Times New Roman", size=70)
        button["font"] = f
        button.grid(column=x, row=y)
        positions[x].append(button)

for row in positions:
    for button in row:
        print (button)

i=0
def edit_button (x,y):
    global i
    i+=1
    if (i%2==0):
        positions[x][y]["text"] = "x"
    else:
        positions[x][y]["text"] = "o"
    print (i)

window.mainloop()

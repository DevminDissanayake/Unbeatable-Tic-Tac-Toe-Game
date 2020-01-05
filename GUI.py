import tkinter
from tkinter import *

# from tkinter.messagebox()
# import tk as tk

window = Tk()
window.title("Tic-Tac-Toe")

Label(window, text="Player 1:").pack(side=TOP)
ent = Entry(window)
ent.pack(side=TOP)
Label(window, text="Player 2:").pack(side=TOP)
ent = Entry(window)
ent.pack(side=TOP)

rootFrame = tkinter.Frame(window, width=1000, height=800, bg="white")
rootFrame.pack()
window = tkinter.Canvas(rootFrame, width=1000, height=800, bg="white")
window.pack()


def draw(win):
    width = 300
    height = 300
    canvas = Canvas(win, background='black', width=width, height=height)

    for line in range(0, width, 100):  # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='white', tags='grid_line_w')

    for line in range(0, height, 100):
        canvas.create_line([(0, line), (width, line)], fill='white', tags='grid_line_h')

    canvas.grid(row=0, column=0)

def btnClick

window.mainloop()

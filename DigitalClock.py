from tkinter import *
from tkinter import font
import datetime

def quit(*args):
    root.destroy()

def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime("%Y-%m-%d / %H:%M:%S"))
    #time = (time.strftime("%H:%M:%S"))
    txt.set(time)

    root.after(1000, clock_time)


root = Tk()
root.attributes("-fullscreen", False)
root.configure(bg = 'black')
root.bind("x", quit)
root.after(1000, clock_time)

fnt = font.Font(family = 'Helvetica', size = 60, weight = 'bold')
txt = StringVar()
lb1 = Label(root, textvariable = txt, font = fnt, fg = 'white', bg = 'black')
lb1.place(relx = 0.5, rely = 0.5, anchor = CENTER)

mainloop()

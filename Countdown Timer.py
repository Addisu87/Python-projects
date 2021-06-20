from tkinter import *
from tkinter import font
import datetime


global endTime

def quit(*args):
    root.destroy()

def not_wait():
    # Get the time remaining until the event
   timeLeft = endTime - datetime.datetime.now()
    #remove the microseconds part
   timeLeft = timeLeft - datetime.timedelta(microseconds = timeLeft.microseconds)
    # Show the time Left
   txt.set(timeLeft)
    # Trigger the countdown after 1000ms
   root.after(1000, not_wait)


root = Tk()
root.attributes("-fullscreen", False)
root.configure(bg = 'black')
root.bind("x", quit)
root.after(1000, not_wait)

# Set the end date and time for the countdown

endTime = datetime.datetime(2021, 9, 30, 9, 0, 0)

fnt = font.Font(family = 'Helvetica', size = 90, weight = 'bold')
txt = StringVar()
lb1 = Label(root, textvariable = txt, font = fnt, fg = 'white', bg = 'black')
lb1.place(relx = 0.5, rely = 0.5, anchor = CENTER)

mainloop()

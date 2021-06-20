from tkinter import *

def calculate():
    temp = int(entry.get())
    temp = 9/5*temp+32
    output_lable.configure(text = 'Converted: {:.1f}'.format(temp))
    entry.delete(0, END)

root = Tk()

message_lable = Label(text = 'Enter a temperature:', font = ('Verdana', 16))
output_lable = Label(font = ('Verdana', 16))
entry = Entry(font = ('Verdana', 16), width = 4)
calc_button = Button(text ='Ok', font = ('Verdana', 16), command = calculate)

message_lable.grid(row = 0, column = 0)
entry.grid(row = 0, column = 1, rowspan = 6, sticky = NE)
calc_button.grid(row = 0, column = 2)
output_lable.grid(row = 1, column = 0, columnspan = 3)

mainloop()

from tkinter import *
from tkinter import ttk

# Main class for calculator
class Application(Frame):
    def __int__(self, master):      # Initialize the frame.
        super(Application, self).__init__(master)
        self.task = " "
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):    # Create all the buttons for calculator.
        # User input stored as an Entry widget.
        self.user_input = ttk.Entry(self, bg = "#5bc8ac", bd= 29, insertwidth = 4, width = 24,
                                    font = ("Verdana", 20, "bold"), textvariable = self.UserIn, justify = RIGHT)
        self.user_input.grid(columnspan = 4)
        self.user_input.insert(0, "0")

        # Button for value 7
        self.button1 = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "7", padx = 33, pady = 25,
                                  font = ("Helvetica", 20, "bold"),  command = lambda: self.button_click(7))
        self.button1.grid(row = 2, column = 0, sticky = W)
        # Button for value 8
        self.button2 = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "8", padx = 33, pady = 25,
                                  font = ("Helvetica", 20, "bold"),  command = lambda: self.button_click(8))
        self.button2.grid(row = 2, column = 1, sticky = W)
        # Button for value 9
        self.button3 = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "9", padx = 33, pady = 25,
                                  font = ("Helvetica", 20, "bold"), command = lambda: self.button_click(9))
        self.button3.grid(row = 2, column = 2, sticky = W)
        # Button for value 4
        self.button4 = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "4", padx = 33, pady = 25,
                                  font = ("Helvetica", 20, "bold"), command = lambda: self.button_click(4))
        self.button4.grid(row = 3, column = 0, sticky = W)
        # Button for value 5
        self.button5 = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "5", padx = 33, pady = 25,
                                  font = ("Helvetica", 20, "bold"), command = lambda: self.button_click(5))
        self.button5.grid(row = 3, column = 1, sticky = W)
        # Button for value 6
        self.button6 = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "6", padx = 33, pady = 25,
                                  font = ("Helvetica", 20, "bold"),  command = lambda: self.button_click(6))
        self.button6.grid(row = 3, column = 2, sticky = W)
        # Button for value 1
        self.button7 = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "1", padx = 33, pady = 25,
                                  font = ("Helvetica", 20, "bold"), command = lambda: self.button_click(1))
        self.button7.grid(row = 4, column = 0, sticky = W)
        # Button for value 2
        self.button8 = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "2", padx = 33, pady = 25,
                                  font = ("Helvetica", 20, "bold"),  command = lambda: self.button_click(2))
        self.button8.grid(row = 4, column = 1, sticky = W)
        # Button for value 3
        self.button9 = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "3", padx = 33, pady = 25,
                                  font = ("Helvetica", 20, "bold"),  command = lambda: self.button_click(3))
        self.button9.grid(row = 4, column = 2, sticky = W)
        # Button value for 0
        self.button10 = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "0", padx = 33, pady = 25,
                                   font = ("Helvetica", 20, "bold"),  command = lambda: self.button_click(0))
        self.button10.grid(row = 5, column = 0, sticky = W)
        # Operator buttons
        # Addition button
        self.Addbutton = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "+", padx = 36, pady = 25,
                                    font = ("Helvetica", 20, "bold"), command = lambda: self.button_click("+"))
        self.Addbutton.grid(row = 2, column = 3, sticky = W)
        # Subtraction button
        self.subbutton = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "-", padx = 39, pady = 25,
                                    font = ("Helvetica", 20, "bold"),  command = lambda: self.button_click("-"))
        self.subbutton.grid(row = 3, column = 3, sticky = W)
        # Multiplicaion button
        self.multibutton = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "*", padx = 38, pady = 25,
                                      font = ("Helvetica", 20, "bold"),  command = lambda: self.button_click("*"))
        self.multibutton.grid(row = 4, column = 3, sticky = W)
        # Division button
        self.divbutton = ttk.Button(self, bg = "#98DBC6", bd = 12, text = "/", padx = 39, pady = 25,
                                    font = ("Helvetica", 20, "bold"),  command = lambda: self.button_click("/"))
        self.divbutton.grid(row = 5, column = 3, sticky = W)
        # Equal button
        self.equalbutton = ttk.Button(self, bg = "#E6D72A", bd = 12, text = "=", padx = 100, pady = 25,
                                      font = ("Helvetica", 20, "bold"), command = self.calculate_task)
        self.equalbutton.grid(row = 5, column = 1, sticky = W, columnspan = 2)
        # Clear button
        self.Clearbutton = ttk.Button(self, bg = "#E6D72A", bd = 12, text = "AC", padx = 7,  width = 28,
                                      font = ("Helvetica", 20, "bold"), command = self.clear_display)
        self.Clearbutton.grid(row = 1, columnspan = 4, sticky = W)

    def button_click(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def calculate_task(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.display_text(self.answer)
            self.task = self.answer
        except SyntaxError as e:
            self.display_text("Invalid Syntax!")
            self.task = " "

    def display_text(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def clear_display(self):
        self.task = " "
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")

calculator  =  Tk ()
calculator.title("Calculator")
app = Application(calculator)
# Make window fixed (cannot be resized) 
calculator.resizable(width = False, height = False)    

calculator.mainloop()

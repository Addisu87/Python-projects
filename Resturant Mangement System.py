import tkinter as tk
import time

localtime = time.asctime(time.localtime(time. time()))

class App1:
    def __init__(self, top):
        self.top = top
        top.title("Restaurant Management")
        top.geometry("1028x500")
        top.configure(background = "#091833")

        font10 = "{Courier New} 14 normal"
        font11 = "{U.S. 101} 30 bold"
        font12 = "Al-Aramco 13 bold"
        font13 = "{Courier New} 12 bold"
        font14 = "{Segoe UI} 14 bold"
        font15 = "Arial 15 bold"
        font16 = "{Segoe UI} 13 bold"

# Title of the cash register
        self. Label1 = tk.Label(master = top, text = 'Restaurant Management System',
                                bg = "#091833", font = font11, fg = "#f2a343")
        self.Label1.place(relx = 0.268, rely = 0.02)

        localtime1 = tk.Label(master = top, text = localtime,  bg = "#091833", font = font10, fg = "steel blue")
        localtime1.place(relx = 0.42, rely = 0.12)

# Label Food
        self. Label2 = tk.Label(master = top, text = 'Order Num: ',  bg = "#091833", font = font12, fg = "#bac8bd")
        self.Label2.place(relx = 0.054, rely = 0.25)
        self. Label2 = tk.Label(master = top, text = 'Fried Potato: ',  bg = "#091833", font = font12, fg = "#bac8bd")
        self.Label2.place(relx = 0.044, rely = 0.32)
        self. Label2 = tk.Label(master = top, text = 'Chk Burger: ',  bg = "#091833", font = font12, fg = "#bac8bd")
        self.Label2.place(relx = 0.053, rely = 0.40)
        self. Label2 = tk.Label(master = top, text = 'Big King: ',  bg = "#091833", font = font12, fg = "#bac8bd")
        self.Label2.place(relx = 0.071, rely = 0.48)
        self. Label2 = tk.Label(master = top, text = 'Chk Royal: ',  bg = "#091833", font = font12, fg = "#bac8bd")
        self.Label2.place(relx = 0.060, rely = 0.56)
        self. Label2 = tk.Label(master = top, text = 'Veg Salad: ',  bg = "#091833", font = font12, fg = "#bac8bd")
        self.Label2.place(relx = 0.059, rely = 0.64)
        self. Label2 = tk.Label(master = top, text = 'Drinks: ',  bg = "#091833", font = font12, fg = "#1812c6")
        self.Label2.place(relx = 0.082, rely = 0.72)

# -------- Entry Food ----------
        self.entry1 = tk.Entry(master = top, bg = "#d9d9d9", fg = "#c60000", selectbackground = "#f2a343", font = font13)
        self.entry1.place(relx = 0.16, rely = 0.24)
        self.entry1 = tk.Entry(master = top, bg = "#d9d9d9", fg = "#c60000", selectbackground = "#f2a343", font = font13)
        self.entry1.place(relx = 0.16, rely = 0.32)
        self.entry1 = tk.Entry(master = top, bg = "#d9d9d9", fg = "#c60000", selectbackground = "#f2a343", font = font13)
        self.entry1.place(relx = 0.16, rely = 0.40)
        self.entry1 = tk.Entry(master = top, bg = "#d9d9d9", fg = "#c60000", selectbackground = "#f2a343", font = font13)
        self.entry1.place(relx = 0.16, rely = 0.48)
        self.entry1 = tk.Entry(master = top, bg = "#d9d9d9", fg = "#c60000", selectbackground = "#f2a343", font = font13)
        self.entry1.place(relx = 0.16, rely = 0.56)
        self.entry1 = tk.Entry(master = top, bg = "#d9d9d9", fg = "#c60000", selectbackground = "#f2a343", font = font13)
        self.entry1.place(relx = 0.16, rely = 0.64)
        self.entry1 = tk.Entry(master = top, bg = "#d9d9d9", fg = "#c60000", selectbackground = "#f2a343", font = font13)
        self.entry1.place(relx = 0.16, rely = 0.72)

# ---------- Calculator ------------
        self.entry2 = tk.Entry(master = top, bg = "#d9d9d9", fg = "#c60000", selectbackground = "#f2a343", font = font13)
        self.entry2.place(relx = 0.702, rely = 0.24, height = 35, relwidth = 0.280)
# --------- Button ----------
        self.Button1 = tk.Button(master = top, text = '''7''', fg = '#122E63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.702, rely = 0.34, height = 44, width = 65)
        self.Button1 = tk.Button(master = top, text = '''8''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.774, rely = 0.34, height = 44, width = 65)
        self.Button1 = tk.Button(master = top, text = '''9''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.846, rely = 0.34, height = 44, width = 65)
        self.Button1 = tk.Button(master = top, text = '''+''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.918, rely = 0.34, height = 44, width = 65)

        self.Button1 = tk.Button(master = top, text = '''4''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.702, rely = 0.44, height = 44, width = 65)
        self.Button1 = tk.Button(master = top, text = '''5''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.774, rely = 0.44, height = 44, width = 65)
        self.Button1 = tk.Button(master = top, text = '''6''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.846, rely = 0.44, height = 44, width = 65)
        self.Button1 = tk.Button(master = top, text = '''-''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.918, rely = 0.44, height = 44, width = 65)

        self.Button1 = tk.Button(master = top, text = '''1''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.702, rely = 0.54, height = 44, width = 65)
        self.Button1 = tk.Button(master = top, text = '''2''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.774, rely = 0.54, height = 44, width = 65)
        self.Button1 = tk.Button(master = top, text = '''3''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.846, rely = 0.54, height = 44, width = 65)
        self.Button1 = tk.Button(master = top, text = '''*''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.918, rely = 0.54, height = 44, width = 65)

        self.Button1 = tk.Button(master = top, text = '''0''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.702, rely = 0.64, height = 44, width = 138)
        self.Button1 = tk.Button(master = top, text = '''.''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.846, rely = 0.64, height = 44, width = 65)
        self.Button1 = tk.Button(master = top, text = '''/''', fg = '#122e63',  bg = '#ffffff', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.918, rely = 0.64, height = 44, width = 65)

        self.Button1 = tk.Button(master = top, text = '''=''', fg = '#e16740',  bg = '#f2a343', font = font14, borderwidth = '0')
        self.Button1.place(relx = 0.702, rely = 0.74, height = 44, width = 287)
# ---------Label Cost ------------
        self. Label3 = tk.Label(master = top, text = 'Cost : ',  bg = "#091833", font = font15, fg = "#e16740")
        self.Label3.place(relx = 0.360, rely = 0.32)
        self. Label3 = tk.Label(master = top, text = 'Service Charge : ',  bg = "#091833", font = font15, fg = "#bac8bd")
        self.Label3.place(relx = 0.340, rely = 0.40)
        self. Label3 = tk.Label(master = top, text = 'Tax : ',  bg = "#091833", font = font15, fg = "#bac8bd")
        self.Label3.place(relx = 0.373, rely = 0.50)
        self. Label3 = tk.Label(master = top, text = 'Sub Total : ',  bg = "#091833", font = font15, fg = "#bac8bd")
        self.Label3.place(relx = 0.357, rely = 0.60)
        self. Label3 = tk.Label(master = top, text = 'Total : ',  bg = "#091833", font = font15, fg = "#bac8bd")
        self.Label3.place(relx = 0.367, rely = 0.70)
# -------- Entry Cost ------
        self.entry3 = tk.Entry(master = top, bg = "#d9d9d9", fg = "#e16740", selectbackground = "#f2a343", font = font13)
        self.entry3.place(relx = 0.415, rely = 0.32)
        self.entry3 = tk.Entry(master = top, bg = "#d9d9d9", fg = "#c60000", selectbackground = "#f2a343", font = font13)
        self.entry3.place(relx = 0.465, rely = 0.40, relwidth = 0.12)
        self.entry3 = tk.Entry(master = top, bg = "#d9d9d9", fg = "#c60000", selectbackground = "#f2a343", font = font13)
        self.entry3.place(relx = 0.416, rely = 0.50)
        self.entry3 = tk.Entry(master = top, bg = "#d9d9d9", fg = "#c60000", selectbackground = "#f2a343", font = font13)
        self.entry3.place(relx = 0.447, rely = 0.60, relwidth = 0.14)
        self.entry3 = tk.Entry(master = top, bg = "#d9d9d9", fg = "#c60000", selectbackground = "#f2a343", font = font13)
        self.entry3.place(relx = 0.419, rely = 0.70)

# ----------- Control Button ----------
        self.Button2 = tk.Button(master = top, text = 'PRICE',  bg = '#e16740', font = font16)
        self.Button2.place(relx = 0.039, rely = 0.86, width = 107, height = 34)
        self.Button2 = tk.Button(master = top, text = 'TOTAL',  bg = '#e16740', font = font16)
        self.Button2.place(relx = 0.155, rely = 0.86, width = 107, height = 34)
        self.Button2 = tk.Button(master = top, text = 'RESET',  bg = '#e16740', font = font16)
        self.Button2.place(relx = 0.270, rely = 0.86, width = 107, height = 34)
        self.Button2 = tk.Button(master = top, text = 'EXIT',  bg = '#091833', font = font16)
        self.Button2.place(relx = 0.386, rely = 0.86, width = 107, height = 34)

root = tk.Tk()

my_gui = App1(root)

root.mainloop()
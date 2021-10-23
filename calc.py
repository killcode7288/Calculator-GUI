from tkinter import *
from tkinter import messagebox
import time




def btn(numbers):
    global opt
    opt = opt + str(numbers)
    text_input.set(opt)

def clear():
    global opt
    opt = ""
    text_input.set("")

def solution():
    global opt
    answer = str(eval(opt))
    text_input.set(answer)
    opt = ""

def mine():
    pass
    
def view():
    pass

def about():
    messagebox.askokcancel('Info', 'Powered by DarlingCorp Technologies Designed by Darlington', icon="info")

def license():
    messagebox.askokcancel('Info', 'Calculator V. 1.0.0.2.3.4', icon="info")

def tips():
    messagebox.askokcancel('Info', 'For tips and tricks visit out site "https//:calculu/tips/learn/.com/h"', icon="info")

def contact():
    messagebox.askokcancel('Info', 'Contact Us via our facebook page on "killcode/calculu/fb"', icon="info")

def wrap():
    messagebox.askokcancel('Thank You', 'Text wrap has been activated your text would be wrapped from now', icon="info")

def tabs():
    messagebox.askokcancel('Info', 'Hide all tabs', icon="info")

def darkmode():
    win.config(bg="black")
    
    


def lightmode():
    pass
    


win = Tk()
win.title("Calculator")
opt = ""
text_input = StringVar()
menu = Menu(win)
win.config(menu=menu)

#filemenu
file_menu = Menu(menu)
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=mine)


#Viewmenu
view_menu = Menu(menu)
menu.add_cascade(label="View",menu=view_menu)
view_menu.add_command(label="Tabs", command=tabs)
view_menu.add_command(label="Text Wrap", command=wrap)


#help_menu
help_menu = Menu(menu)
menu.add_cascade(label="Help",menu=help_menu) 
help_menu.add_command(label="Contact Us",command=contact)
help_menu.add_command(label="Tips and Tricks",command=tips)
help_menu.add_command(label="View license",command=license)
help_menu.add_command(label="About",command=about)

#Appearance
theme_menu = Menu(menu)
menu.add_cascade(label="Appearance", menu=theme_menu)
theme_menu.add_command(label="Toggle Darkmode", command=darkmode)
theme_menu.add_command(label="Toggle Lightmode", command=lightmode)



#Exit
exit_menu = Menu(menu)
menu.add_command(label="Exit", command=win.quit)





textDisplay = Entry(win, font=('arial 20 bold'), textvariable=text_input, bd=30,insertwidth=4,
bg="powder blue", justify="right") .grid(columnspan=4)

btn_7 = Button(win, padx=16,pady=15, bd=8, fg="black",cursor="hand2", font=("arial 20 bold"),text="7", command=lambda:btn(7)) .grid(row=1, column=0)

btn_8 = Button(win, padx=16, bd=8,pady=15, fg="black",cursor="hand2", font=("arial 20 bold"),text="8", command=lambda:btn(8)) .grid(row=1, column=1)

btn_9 = Button(win, padx=16, bd=8,pady=15, fg="black", cursor="hand2",font=("arial 20 bold"),text="9", command=lambda:btn(9)) .grid(row=1, column=2)

Addition = Button(win, padx=16, bd=8,pady=15, fg="black",cursor="hand2", font=("arial 20 bold"),text="+", command=lambda:btn("+")) .grid(row=1, column=3)


btn_4 = Button(win, padx=16, bd=8,pady=15, fg="black",cursor="hand2", font=("arial 20 bold"),text="4", command=lambda:btn(4)) .grid(row=2, column=0)

btn_5 = Button(win, padx=16, bd=8,pady=15, fg="black", cursor="hand2",font=("arial 20 bold"),text="5", command=lambda:btn(5)) .grid(row=2, column=1)

btn_6 = Button(win, padx=16, bd=8,pady=15, fg="black",cursor="hand2", font=("arial 20 bold"),text="6",command=lambda:btn(6)) .grid(row=2, column=2)

Subtraction = Button(win, padx=16, bd=8,pady=15, fg="black",cursor="hand2", font=("arial 20 bold"),text="−",command=lambda:btn("-")) .grid(row=2, column=3)


btn_1 = Button(win, padx=16, bd=8,pady=15, fg="black", cursor="hand2",font=("arial 20 bold"),text="1", command=lambda:btn(1)) .grid(row=3, column=0)

btn_2 = Button(win, padx=16, bd=8,pady=15, fg="black",cursor="hand2", font=("arial 20 bold"),text="2", command=lambda:btn(2)) .grid(row=3, column=1)

btn_3 = Button(win, padx=16, bd=8,pady=15, fg="black",cursor="hand2", font=("arial 20 bold"),text="3", command=lambda:btn(3)) .grid(row=3, column=2)

Multiplication = Button(win, padx=16,pady=15, bd=8, fg="black",cursor="hand2", font=("arial 20 bold"),text="x", command=lambda:btn("*")) .grid(row=3, column=3)


btn_0 = Button(win, padx=16, bd=8,pady=15, fg="black",cursor="hand2", font=("arial 20 bold"),text="0",command=lambda:btn(0)) .grid(row=4, column=0)

clear = Button(win, padx=16, bd=8,pady=15, fg="black",cursor="hand2",font=("arial 20 bold"),text="C",command=clear) .grid(row=4, column=1)

equal_to = Button(win, padx=16, bd=8,pady=15, fg="black",cursor="hand2", font=("arial 20 bold"),text="=", command=solution) .grid(row=4, column=2)

Division = Button(win, padx=16, bd=8,pady=15, fg="black",cursor="hand2", font=("arial 20 bold"),text="÷", command=lambda:btn("/")) .grid(row=4, column=3)


win.mainloop()
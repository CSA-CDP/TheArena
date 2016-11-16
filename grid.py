#Collin Patterson
#Mr. Davis
#10/7/2016
#Advanced Computer Programming

from tkinter import *
from tkinter import ttk

def clearframe():
    usrnme_entry.delete(0,'end')
    psswrd_entry.delete(0,'end')

root = Tk()

topMenu = Menu(root)
root.config(menu=topMenu)

subMenu = Menu(topMenu)
topMenu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='Exit', command=root.quit)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

usrnme = StringVar()
psswrd = StringVar()

usrnme_entry = ttk.Entry(mainframe, width=10, textvariable=usrnme)
usrnme_entry.grid(column=1, row=0, pady=4, sticky=W)
psswrd_entry = ttk.Entry(mainframe, width=10, textvariable=psswrd)
psswrd_entry.grid(column=1, row=1, pady=4, sticky=W)

ttk.Label(mainframe, text="Username").grid(column=0, row=0, sticky=W, pady=4)
ttk.Label(mainframe, text="Password").grid(column=0, row=1, sticky=W, pady=4)

submit_button = ttk.Button(mainframe, text="Login", width=20, command=clearframe)
submit_button.grid(column=1, row=2, pady=4, columnspan=2)

root.mainloop()
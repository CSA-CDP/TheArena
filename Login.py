#Collin Patterson
#10/2/2016
#Mr. Davis
#Advanced Computer Programming
from tkinter import *

def doNothing(): #default function for now
    print('ok ok I wont...')

def forgot(): #Forgot password function
    print('You for got it!')

def about():
    print('About')

root = Tk()

topMenu = Menu(root)
root.config(menu=topMenu)


subMenu = Menu(topMenu)
topMenu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='Exit', command=root.quit)

editMenu = Menu(topMenu)
topMenu.add_cascade(label='Help', menu=editMenu)
editMenu.add_command(label='Forgot Password', command=forgot)
editMenu.add_command(label='About', command=about)

#Toolbar

toolbar = Frame(root)


printBtn=Button(toolbar, text='Login', command=doNothing)
printBtn.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

root.mainloop()
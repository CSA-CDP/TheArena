#Collin Patterson
#9/29/2016
#Mr. Davis
#Advanced Computer Programming
from tkinter import *


def doNothing(): #default function for now
    print('ok ok I wont...')

root = Tk()

#Main Menu

topMenu = Menu(root)
#Creates menu and submenus, File, New project, New, and Exit. submenu Edit will have ubdo
root.config(menu=topMenu)


subMenu = Menu(topMenu)
topMenu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='New Project...', command=doNothing)
subMenu.add_command(label='New...', command=doNothing)
subMenu.add_separator() #seprates new commands from exit
subMenu.add_command(label='Exit', command=root.quit)

editMenu = Menu(topMenu)
topMenu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Undo', command=doNothing)

#Toolbar

toolbar = Frame(root, bg='blue')

insertBtn = Button(toolbar, text='Insert image', command=doNothing)
insertBtn.pack(side=LEFT, padx=2, pady=2)
printBtn=Button(toolbar, text='Print', command=doNothing)
printBtn.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

root.mainloop()
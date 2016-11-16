# Collin Patterson
# Mr. Davis
# 10/7/2016
# Advanced Computer Programming


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time


def aboutprint():
    messagebox.showinfo(title='Travel Log', message='Version .1')


def Submit():
    p.configure(value=100)
    # try:
    # listboxselection = int(l.curselection()[0])
    # listValue=str(l[listboxselection])
    # if listValue == 'Australia' or listValue == 'Barbados' or listValue == 'Canada' or listValue == 'France' or listValue == 'Germany' or listValue == 'Japan' or listValue == 'Peru' or listValue == 'Russia' or listValue == 'Swaziland' or listValue == 'Turkey' or listValue == 'UK':
    #  p.configure(value=100)
    # else:
    # pass
    # except:
    # pass

def Clear():
    #work on this
    print('Hi')


root = Tk()

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))

topMenu = Menu(root)
root.config(menu=topMenu)

subMenu = Menu(topMenu)
topMenu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='Exit', command=root.quit)

editMenu = Menu(topMenu)
topMenu.add_cascade(label='Help', menu=editMenu)
editMenu.add_command(label='About', command=aboutprint)

submitbtn = ttk.Button(root, text="Submit", command=Submit)
submitbtn.grid(column=2, row=0, sticky=(N))

clearbtn = ttk.Button(root, text="Clear", command=Clear)
clearbtn.grid(column=2, row=0, sticky=(W,E))

l = Listbox(root, height=10)
l.grid(column=0, row=0)
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(N, S))
l['yscrollcommand'] = s.set
ttk.Sizegrip().grid(column=1, row=1, sticky=(S, E))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
for i in range(1, 2):
    l.insert('end', 'Australia', 'Barbados', 'Canada', 'France', 'Germany', 'Japan', 'Peru', 'Russia', 'Swaziland ',
             'Turkey', 'UK')

t = Text(root, width=15, height=10)
t.grid(column=0, row=1, sticky=(N, S))
t.insert('end', 'Add Description(Remove text before typing)')

p = ttk.Progressbar(root, orient=VERTICAL, length=200, mode='determinate', value=0)
p.grid(column=3, row=0)

root.mainloop()





# Collin Patterson
# Mr. Davis
# 10/7/2016
# Advanced Computer Programming

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

root = Tk()

global daytonHealth1
global riveraHealth2
daytonHealth1 = int(100)
riveraHealth2 = int(100)

list1 = ('Attack', 'Defend', 'Special')
list2 = ('Attack', 'Defend', 'Special')

listvar1 = StringVar(value=list1)
listvar2 = StringVar(value=list2)


def aboutprint():
    messagebox.showinfo(title='Math Wars', message='Version .1')


def Fight():
    global daytonHealth1
    global riveraHealth2
    Attack1 = random.randint(1, 10)
    Attack2 = random.randint(1, 10)
    specialAttack1 = random.randint(10, 20)
    specialAttack2 = random.randint(10, 20)
    try:
        listboxselection1 = int(listbox1.curselection()[0])
        listboxselection2 = int(listbox2.curselection()[0])
        value1 = str(list1[listboxselection1])
        value2 = str(list2[listboxselection2])
        if value1 == 'Attack':
            if value2 == 'Attack':
                print('Mr. Rivera attacked Mr. Dayton!')
                daytonHealth1 = (daytonHealth1 - Attack1)
                print(daytonHealth1)
                print('')
                print('Mr. Dayton attacked Mr. Rivera!')
                riveraHealth2 = (riveraHealth2 - Attack2)
                print(riveraHealth2)
                print('------------------------------------------------------------------------------')
            elif value2 == 'Defend':
                print('Mr. Dayton was immune!')
                print('------------------------------------------------------------------------------')
            elif value2 == 'Special':
                print('Mr. Rivera attacked Mr. Dayton!')
                daytonHealth1 = (daytonHealth1 - Attack1)
                print(daytonHealth1)
                print('')
                print('Mr. Dayton attacked Mr. Rivera using his special move "Flaming 4 Square Ball"!')
                riveraHealth2 = (riveraHealth2 - specialAttack1)
                print(riveraHealth2)
                print('------------------------------------------------------------------------------')
            else:
                pass
        elif value1 == 'Defend':
            if value2 == 'Attack':
                print('Mr. Rivera was immune!')
                print('------------------------------------------------------------------------------')
            elif value2 == 'Defend':
                print('Both teachers were immune!')
                print('------------------------------------------------------------------------------')
            elif value2 == 'Special':
                print('Mr. Rivera was immune!')
                print('------------------------------------------------------------------------------')
            else:
                pass
        elif value1 == 'Special':
            if value2 == 'Attack':
                print('Mr. Rivera attacked Mr. Dayton using his special move "Exploding Kittens"!')
                daytonHealth1 = (daytonHealth1 - specialAttack1)
                print(daytonHealth1)
                print('')
                print('Mr. Dayton attacked Mr. Rivera!')
                riveraHealth2 = (riveraHealth2 - Attack1)
                print(riveraHealth2)
                print('------------------------------------------------------------------------------')
            elif value2 == 'Defend':
                print('Mr. Dayton was immune!')
                print('------------------------------------------------------------------------------')
            elif value2 == 'Special':
                print('Mr. Rivera attacked Mr. Dayton using his special move "Exploding Kittens"!!')
                daytonHealth1 = (daytonHealth1 - specialAttack1)
                print(daytonHealth1)
                print('')
                print('Mr. Dayton attacked Mr. Rivera using his special move "Flaming 4 Square Ball"!')
                riveraHealth2 = (riveraHealth2 - specialAttack2)
                print(riveraHealth2)
                print('------------------------------------------------------------------------------')
        else:
            pass


        if daytonHealth1 <= 0 and riveraHealth2 <= 0:
            messagebox.showinfo(title='Winner', message='Both teachers lost!')
            winner.configure(text='No one')
            fightbtn.configure(state='disabled')
        elif riveraHealth2 <= 0:
            winner.configure(text='Mr. Dayton!')
            fightbtn.configure(state='disabled')
            messagebox.showinfo(title='Winner', message='Mr. Dayton over crit Mr. Rivera!')
        elif daytonHealth1 <= 0:
            winner.configure(text='Mr. Rivera')
            fightbtn.configure(state='disabled')
            messagebox.showinfo(title='Winner', message='Mr. Rivera over crit Mr. Dayton!')
        else:
            pass

    except:
        pass


mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))

topMenu = Menu(root)
root.config(menu=topMenu)

subMenu = Menu(topMenu)
topMenu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='Exit', command=root.quit)

editMenu = Menu(topMenu)
topMenu.add_cascade(label='Help', menu=editMenu)
editMenu.add_command(label='About', command=aboutprint)

fightbtn = ttk.Button(root, text="Fight", command=Fight)
listbox1 = Listbox(root, listvariable=listvar1, selectmode='single', exportselection=0, height=10)
listbox2 = Listbox(root, listvariable=listvar2, selectmode='single', exportselection=0, height=10)
attack1 = ttk.Label(root, text='Attack: 1-10')
attack2 = ttk.Label(root, text='Attack: 1-10')
defence1 = ttk.Label(root, text='Defends: 3')
defence2 = ttk.Label(root, text='Defends: 3')
special1 = ttk.Label(root, text='Special: Exploding Kittens')
special2 = ttk.Label(root, text='Special: Flaming 4 Square')
player1 = ttk.Label(root, text='Mr. Rivera')
player2 = ttk.Label(root, text='Mr. Dayton')
wins = ttk.Label(root, text='Wins')
winner = ttk.Label(root, text='')

fightbtn.grid(column=1, row=4, sticky=S)
listbox1.grid(column=0, row=1, rowspan=3)
listbox2.grid(column=2, row=1, rowspan=3)
attack1.grid(column=0, row=4)
attack2.grid(column=2, row=4)
defence1.grid(column=0, row=5)
defence2.grid(column=2, row=5)
special1.grid(column=0, row=6)
special2.grid(column=2, row=6)
player1.grid(column=0, row=0)
player2.grid(column=2, row=0)
wins.grid(column=1, row=1)
winner.grid(column=1, row=2)

root.mainloop()



#Collin Patterson
#9/2/2016
#Mr. Davis 
#Advance Computer Programming
from tkinter import *
from tkinter import ttk

def Total(*args):
    try:
        value = float(Item.get())
        Total.set(value)
    except ValueError:
        pass
    
root=Tk()
root.title("Order Form")

mainframe = ttk.Frame(root, padding="2 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

Item = StringVar()
Shipping = StringVar()
Tax = StringVar()

Item_entry = ttk.Entry(mainframe, width=10, textvariable=Item)
Item_entry.grid(column=1, row=1, sticky=(W, E))

Shipping_entry = ttk.Entry(mainframe, width=10, textvariable=Shipping)
Shipping_entry.grid(column=1, row=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=Total).grid(column=2, row=4, sticky=(W, E))
ttk.Button(mainframe, text="Total:", command=Total).grid(column=1, row=4, sticky=W)

ttk.Label(mainframe, text="Item").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="Shipping days").grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="Tax").grid(column=2, row=3, sticky=W)
ttk.Label(mainframe, text="%8.25").grid(column=1, row=3, sticky=W)

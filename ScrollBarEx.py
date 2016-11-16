# Collin Patterson
# Mr. Davis
# 10/7/2016
# Advanced Computer Programming


from tkinter import *
from tkinter import ttk
root = Tk()
l1 = Listbox(root, height=5)
l2 = Listbox(root, height=5)
l1.grid(column=0, row=0, sticky=(N,W,E,S))
l2.grid(column=2, row=0, sticky=(N,W,E,S))
s1 = ttk.Scrollbar(root, orient=VERTICAL, command=l1.yview)
s2 = ttk.Scrollbar(root, orient=VERTICAL, command=l2.yview)
s1.grid(column=0, row=0, sticky=(N,S))
s2.grid(column=1, row=0, sticky=(N,S))
l1['yscrollcommand'] = s2.set
l2['yscrollcommand'] = s1.set
ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

p = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate', value=10)
p.grid(column=0, row=2, sticky=(N,S))


for i in range(1, 101):
   l1.insert('end', 'Line %d of 100' % i)
   l2.insert('end', 'Line %d of 100' % i)
root.mainloop()





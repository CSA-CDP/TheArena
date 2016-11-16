
from tkinter import *
from tkinter import ttk
import getpass
from tkinter import messagebox
import csv
import time
import os
import re
import hashlib
#import RPi.GPIO as io
from datetime import datetime
# io.setmode(io.BCM)
# pir_pin = 24
# power_pin = 27
# os.system("clear")
# io.setup(pir_pin, io.IN)
# io.setup(power_pin, io.OUT)
# io.output(power_pin, False)
# PERIOD_OF_TIME = 1800

def forgotpasswordvar(): #default function
    print("you forgot it!")

root = Tk()
root.title("Login")

def loginoffline(*args):
    try:
        var1=False
        username=usernamevar.get()
        password=passwordvar.get()
        f2 = open('hashd.csv', 'r')
        f = open("Logins.txt","a")
        students=csv.reader(f2)
        username_rowgetnumyo=2 #change host_row to the corresponding row - 1 (ie; row 45, put in 44) in google's csv
        password_rowgetnum=3 #master_row to the schools student list
        salt="gnuvie:^)"
        for hosts_rowyo in students:
            row = 1
            username=username.replace("@chaparralstaracademy.com","")
            hosts_rowyo[username_rowgetnumyo]=hosts_rowyo[username_rowgetnumyo].replace("@chaparralstaracademy.com","")
            hosts_rowyo[username_rowgetnumyo]=hosts_rowyo[username_rowgetnumyo].zfill(4)
            #print(str(hashlib.sha256(username.encode("UTF-8")).hexdigest())+" username "+hosts_rowyo[username_rowgetnumyo]+"\n"+str(hashlib.sha256(password.encode("UTF-8")).hexdigest())+" password "+hosts_rowyo[password_rowgetnum])
            if(username=="displayport:^)"):
                exit()
            if (hashlib.md5((salt+username).encode("UTF-8")).hexdigest() == hosts_rowyo[username_rowgetnumyo]) & (hashlib.md5((salt+password).encode("UTF-8")).hexdigest() == hosts_rowyo[password_rowgetnum]):
                messagebox.showinfo("", "Logging in complete!")
                f.write(username+" "+str(datetime.now())+"\n")
                f.close()
                user_entry.delete(0, "end")
                passwd_entry.delete(0, "end")
                start = time.time()
                while True :
                    # io.output(power_pin, True)
                    #
                    # if time.time() > start + PERIOD_OF_TIME:
                    #     print("POWER OFF")
                    #     time.sleep(1)
                    #     io.output(power_pin, False)
                    #     time.sleep(3)
                    #     loginoffline()
                    #     break
                    loggingin.set("Logged in!")
                    var1=True
                    break
                break
        if var1==False:
            messagebox.showinfo("","Invalid username or password, please try again! ")
            user_entry.delete(0, 'end')
            passwd_entry.delete(0, 'end')
            loggingin.set("")
            f2.close()
            f.close()
    except KeyboardInterrupt:
        messagebox.showinfo("","Invalid, please try again!")


usernamevar = StringVar()
passwordvar = StringVar()
loggingin=StringVar()

mainframe = Frame(root, width=300, height=300)

#******** Entries **********
content = Frame(root)
frame = Frame(content, borderwidth=5, relief="sunken", width=300, height=175)
usernamelbl=Label(content,text="Enter username below")
usernamelbl.pack( padx=2, pady=2 )
user_entry=Entry(content, width=25, textvariable=usernamevar)
user_entry.pack(padx=2, pady=2 )
passwdlbl=Label(content, text="Enter password below")
passwdlbl.pack(padx=2, pady=2 )
passwd_entry=Entry(content, width=25, show='*', textvariable=passwordvar)
passwd_entry.pack(padx=2, pady=2 )

content.pack(padx=2, pady=2 )

loginbutton=Button(content, text="Login", command=loginoffline)
loginbutton.pack(padx=2, pady=2)

logginginlbl=Label(content,textvariable=loggingin)
logginginlbl.pack()

user_entry.focus()
root.bind('<Return>', loginoffline)
root.mainloop()


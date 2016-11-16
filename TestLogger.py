import getpass
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
def loginoffline():
    try:
        f2 = open('hashd.csv', 'r')
        f = open("Logins.txt","a")
        students=csv.reader(f2)
        username=input("Please enter your username: ")
        password=getpass.getpass("Please enter your password: ")
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
                # print("Logging in.", end=""),
                # time.sleep(1)
                # print(".", end=""),
                # time.sleep(1)
                # print(".")
                # time.sleep(3)
                # os.system("clear")
                print("Logging in complete! Plug in your chromebook now;")
                f.write(username+" "+str(datetime.now())+"\n")
                f.close()
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
                    print("It works!")
                    break
                break
        # print("Logging in.", end=""),
        # time.sleep(1)
        # print(".", end=""),
        # time.sleep(1)
        # print(".")
        # time.sleep(3)
        # os.system("clear")
        print("Error logging in, please try again! ")
        loginoffline()
        f2.close()
        f.close()
    except KeyboardInterrupt:
        print("Error, please try again! ")
        loginoffline()

loginoffline()

import os
import random
import threading
from time import sleep
import requests
from colorama import Fore, Back, Style
import rich


print (f"""
    
 __   __ _____            ____                  _               
 \ \ / // ____|          |  _ \                | |              
  \ V /| (___    ______  | |_) | ___  _ __ ___ | |__   ___ _ __ 
   > <  \___ \  |______| |  _ < / _ \| '_ ` _ \| '_ \ / _ |  __|
  / . \ ____) |          | |_) | (_) | | | | | | |_) |  __| |   
 /_/ \_|_____/           |____/ \___/|_| |_| |_|_.__/ \___|_|  
                                                                                   

>>> github.com/XSBacon
    
    


 """)
sleep(5)
print(f"""
Starting Server..
v1.0
""")
sleep (5)
print(f"""
Executing XS PROTECT Script..
v1.0
""")
print(""" 
Starting Spam Bomber Menu
v1.0
""")
sleep(3)
os.system("cls")
# load up the main
LINK = input("Enter the discord webhook url: ")
sleep(2)
os.system("cls")
MSG = input("Enter the message you want to spam with mention everyone: ")
print("Starting to spam...")
sleep(2)
os.system("cls")
def send_message(link, msg):
    print(f"Sending message ...")
    try:
        requests.post(link, data={"content": f"@here\n{msg}", "username": random.randint(123, 12318248124)})
        print("Message sent!")
    except:
        pass
while True:
    t = threading.Thread(target=send_message, args=(LINK, MSG))
    t.start()



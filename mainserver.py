import os
import random
import threading
from time import sleep
import requests



color 0A

print (f"""
                                                           
               github.com/XSSBACON                     

""")
sleep(2)
print(f"""
Starting Server..
v1.0
""")
print(f"""
Executing XS PROTECT Script..
v1.0
""")
print(""" 
Starting Spam Bomber Menu

v1.0
""")
sleep(0.1)
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

import os
import random
import threading
from time import sleep
import requests



color 0A

print (f"""
                     $$\                                               
                    $$ |                                              
$$\   $$\  $$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\  $$$$$$$\  
\$$\ $$  |$$  _____|$$  __$$\  \____$$\ $$  _____|$$  __$$\ $$  __$$\ 
 \$$$$  / \$$$$$$\  $$ |  $$ | $$$$$$$ |$$ /      $$ /  $$ |$$ |  $$ |
$$  $$<   \____$$\ $$ |  $$ |$$  __$$ |$$ |      $$ |  $$ |$$ |  $$ |
$$  /\$$\ $$$$$$$  |$$$$$$$  |\$$$$$$$ |\$$$$$$$\ \$$$$$$  |$$ |  $$ |
\__/  \__|\_______/ \_______/  \_______| \_______| \______/ \__|  \__|
                                                                      
                                                                      
               github.com/XSSBACON                     

""")

print(f"""

XS Bacon
Ghalbeyou presents ...
""")
sleep(2)
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

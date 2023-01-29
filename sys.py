import pyautogui
import os
import time
from time import sleep
import pyfiglet
from rich.console import Console
import tkinter
from tkinter import messagebox


con = Console()
def userchat():
    while True:
        user = input("Whats your fav food : ")
        if user.isalpha():
            user = input(user)
            break
        else:
            con.print("You cant use numbers\nTry agian ",style="bold red")

userchat()

hacker = Console()

def main():
    while True:
        password = input("whats your number : ")
        if password.isdigit():
            password = input(password)
            break
        else:
            hacker.print("You cant use alfabet key",style="bold green")
            
main()   

color1 = Console()
color2 = Console()
color3 = Console()
color1.print('Thank you ',style="bold red") ; sleep(1.6)
color2.print('Your infomation has sumited',style="bold red") ; sleep(1.6)
color3.print("bye bye have a gooday",style="bold red ") ; sleep(1.6)




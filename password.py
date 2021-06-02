import random 
from os import system, name
import sys
import pyperclip

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def password_generator():
    letters = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
    numbers = ['1234567890']
    characters = ['!@#$%^&*()-=|"\\""//",.:[]']

    mix = letters + numbers + characters
    mix = str(mix)

    x = input("How long do you want your password to be?: ")
    x = int(x)

    password = ""

    for i in range(0, x):
        password += random.choice(mix)
        print(password)

    while(True):
        pyperclip.copy(password)
        print("password was saved to clipboard!")
        print("Your password is: " + password)
        generate = input("do you want to generate another password y or n: ")

        if generate == "y":
            password_generator()
        if generate =="n":
            clear()
            sys.exit(0)
        else:
            continue

password_generator()

import tkinter as tk
from tkinter import *
import random


root = tk.Tk()
def correct(inp):
    if inp.isdigit():
        return True
    else:
        return False

root.geometry("250x250")
root.configure(bg = "white")

L1 = tk.Label(root, text = "Guess a number from 1-10")
L1.pack()
E1 = tk.Entry(root, bd = 5)
E1.pack()
B1 = tk.Button(root, text = "Guess", bd = 5, bg = "white",)
B1.pack()

reg = root.register(correct)
E1.config(validate="key", validatecommand=(reg, '%P'))

num = random.randint(0, 11)
print(random.randint)


 
while E1 != num:
   print("Incorrect!")
   print("Please guess again!")
print("Correct!")
break


root.mainloop()
import random

import tkinter as tk

root = tk.Tk()

rand_num = random.randint(0, 2)

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

label1 = tk.Label(root, text='Rock Paper Scissors')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Make your choice: ')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def make_choice():
    x1 = entry1.get()

    label3 = tk.Label(root, text=10)
    canvas1.create_window(200, 210, window=label3)

player = input("Make your move: ").lower()
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}" )
if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "paper":
        print("Computer wins!")
    elif computer == "scissors":
        print("You win!")
elif player == "paper":
    if computer == "rock":
        print("You win!")
    elif computer == "scissors":
        print("Computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("You win!")
    elif computer == "rock":
        print("Computer wins!")
else:
    print("Something went wrong")



from tkinter import *
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 400)
canvas1.pack()


label1 = tk.Label(root, text='Think of A Number')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type your Number:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getNumber():

    x1 = entry1.get()

    label3 = tk.Label(root, text= f'{x1} x 2 = ' +  'is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    
    label4 = tk.Label(root, text= int(x1)*2,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)

    label5 = tk.Label(root, text = (" / 2 ="))



button1 = tk.Button(text='Pick a number and dont tell anyone', command=getNumber, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)


root.mainloop()
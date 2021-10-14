import tkinter as tk
import requests


#Functions

def usdToYuan():
    #yuan = ( float(yuanToUSD.get("1.0", "end")) * 6.47)
    yuan = (float(conversion.get("1.0", "end-1c")) * 6.47)
    btn_load.config(text=f"The conversion is roughly {yuan} yuan")

def yuanToUSD():
    dollars = (float(conversion.get("1.0","end-1c")) * 0.15)
    btn_load2.config(text=f"The conversion is roughly {dollars} usd")


#Format Window

window = tk.Tk()
window.geometry("800x600")
window.title("Currency Conversion")
window.config(padx=5,pady=5,background="#E1C1F5")

title_label = tk.Label(window, text = "Currency Conversion")
title_label.config(font=("Arial",16))
title_label.pack(padx=5,pady=5)

btn_load = tk.Button(window,text="Convert to CNY", command=usdToYuan)
btn_load.config(font=("Arial",20))
btn_load.pack(padx=10,pady=10)

btn_load2 = tk.Button(window,text="Convert to USD", command=yuanToUSD)
btn_load2.config(font=("Arial",20))
btn_load2.pack(padx=10,pady=10)



conversion = tk.Text(window,height=1,width=20)
conversion.config(font=("Arial",10))
conversion.pack(padx=5,pady=5)






window.mainloop()



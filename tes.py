import tkinter as tk
from tkinter import messagebox
import winsound as ws

x = 200

def button_func(event):
    melo = event.widget["text"]
    if melo == "ド":
        ws.Beep(262,x)
    elif melo == "レ":
        ws.Beep(277,x)
    else:
        pass


#最初の画面
base = tk.Tk()
base.geometry("700x700")
base.title("占いアプリ")
button = tk.Button(base,text="ド",width=10,height=10)
button.place(x=70, y=300)
button.bind("<1>",button_func)
button2 = tk.Button(base,text="レ",width=10,height=10)
button2.place(x=140, y=300)
base.mainloop()
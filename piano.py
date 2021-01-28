import tkinter as tk
from tkinter import messagebox
import winsound as ws




def button_me():
    ws.Beep(262,200)
def button_me_():
    ws.Beep(277,200)
def button_me2():
    ws.Beep(294,200)
def button_me2_():
    ws.Beep(311,200)
def button_me3():
    ws.Beep(330,200)
def button_me4():
    ws.Beep(349,200)
def button_me4_():
    ws.Beep(370,200)
def button_me5():
    ws.Beep(392,200)
def button_me5_():
    ws.Beep(415,200)
def button_me6():
    ws.Beep(440,200)
def button_me6_():
    ws.Beep(466,200)
def button_me7():
    ws.Beep(494,200)
def button_me8():
    ws.Beep(523,200)



base = tk.Tk()
base.geometry("800x700")
base.title("ピアノ")
buttonl = tk.Button(base,text="ド",width=8,height=10,command=button_me)
buttonl.place(x=70, y=300)
buttonl_ = tk.Button(base,text="ド＃",bg="black",fg="white",width=8,height=10,command=button_me_)
buttonl_.place(x=105, y=140)
buttonl2 = tk.Button(base,text="レ",width=8,height=10,command=button_me2)
buttonl2.place(x=140, y=300)
buttonl2_ = tk.Button(base,text="レ#",bg="black",fg="white",width=8,height=10,command=button_me2_)
buttonl2_.place(x=175, y=140)
buttonl3 = tk.Button(base,text="ミ",width=8,height=10,command=button_me3)
buttonl3.place(x=210, y=300)
buttonl4 = tk.Button(base,text="ファ",width=8,height=10,command=button_me4)
buttonl4.place(x=280, y=300)
buttonl4_ = tk.Button(base,text="ファ#",bg="black",fg="white",width=8,height=10,command=button_me4_)
buttonl4_.place(x=320, y=140)
buttonl5 = tk.Button(base,text="ソ",width=8,height=10,command=button_me5)
buttonl5.place(x=350, y=300)
buttonl5_ = tk.Button(base,text="ソ#",bg="black",fg="white",width=8,height=10,command=button_me5_)
buttonl5_.place(x=390, y=140)
buttonl6 = tk.Button(base,text="ラ",width=8,height=10,command=button_me6)
buttonl6.place(x=420, y=300)
buttonl6_ = tk.Button(base,text="ラ#",bg="black",fg="white",width=8,height=10,command=button_me6_)
buttonl6_.place(x=460, y=140)
buttonl7 = tk.Button(base,text="シ",width=8,height=10,command=button_me7)
buttonl7.place(x=490, y=300)
buttonl8 = tk.Button(base,text="ド",width=8,height=10,command=button_me8)
buttonl8.place(x=560, y=300)
base.mainloop()
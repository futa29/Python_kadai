import tkinter as tk

ans = 0
hugo = 0

def one():
    lbl['text'] = '１'
    global ans
    global hugo
    if hugo == 0 or hugo == 1:
        ans += 1
    else:
        ans -= 1

def two():
    lbl['text'] = '２'
    global ans
    global hugo
    if hugo == 0 or hugo == 1:
        ans += 2
    else:
        ans -= 2

def plus():
    global ans
    global hugo
    hugo = 1
    lbl['text'] = ans

def minus():
    global ans
    global hugo
    hugo = 2
    lbl['text'] = ans

def equal():
    global ans
    global hugo
    if hugo == 0: #アプリ起動直後に＝が押された際の対応
        lbl['text'] = ''
    else:
        lbl['text'] = ans

def reset():
    lbl['text'] = ''
    global ans
    global hugo
    ans = 0
    hugo = 0

base = tk.Tk()
base.title('電 卓')
base.geometry('450x550')

lbl = tk.Label(text='', height=2, width=10, font=('',30), bg='white')
lbl.pack(anchor='center')
lbl.place(x=120, y=50)
btn1 = tk.Button(text=' １ ', height=1, width=5, font=('',30), command=one)
btn1.place(x=100, y=160)
btn2 = tk.Button(text=' ２ ', height=1, width=5, font=('',30), command=two)
btn2.place(x=100, y=250)
btn3 = tk.Button(text=' ＋ ', height=1, width=5, font=('',30), command=plus)
btn3.place(x=240, y=160)
btn4 = tk.Button(text=' ー ', height=1, width=5, font=('',30), command=minus)
btn4.place(x=240, y=250)
btn5 = tk.Button(text=' ＝ ', height=1, width=5, font=('',30), command=equal)
btn5.place(x=170, y=340)
btn6 = tk.Button(text=' リセット ', height=1, width=6, font=('',30), command=reset)
btn6.place(x=160, y=430)

base.mainloop()

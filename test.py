import tkinter as tk
import random as ra

#占いリスト
uranai_list = ["大吉","中吉","吉","凶"]



def base_view():

    #占いボタンが押された時、最初の画面を消し、次の画面を生成
    def ura_button():
        base.destroy()
        next_view()
        
    #表示
    base = tk.Tk()
    base.geometry("300x300")
    base.title("占いアプリ")
    input_label = tk.Label(base,text="★占いアプリ★")
    input_label.place(x=110, y=100)

    #ボタン
    button = tk.Button(base,text=" 占 う",command=ura_button)
    button.place(x=120, y=160)
    base.mainloop()

def next_view():
    
    #戻るボタンが押された時、今の画面を消す
    def return_button():
        next.destroy()
        base_view()

    
    #チョイスで占いリストから、ランダムで値を取得する
    ura = ra.choice(uranai_list)

    #表示
    next = tk.Tk()
    next.geometry("300x300")
    next.title("結果画面")
    input_label = tk.Label(next,text=ura)
    input_label.place(x=130, y=100)

    #ボタン
    button = tk.Button(next,text="戻る",command=return_button)
    button.place(x=120, y=160)
    next.mainloop()



#最初の画面の実行
base_view()

























# count=0
# for i in range(1,10):
#     for j in range(1,10):
#         #インクリメントは+=
#         count+=1
#         print(i*j)



# #str()で文字列にするのを忘れずに       
# print('表示個数'+str(count))    
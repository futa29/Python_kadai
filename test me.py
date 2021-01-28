import winsound  as ws #モジュールwsのインポート
from  msvcrt import getch

duration_ms=300 #音の持続時間(ms) 

def play_pitch(x,duration_ms):
    ws.Beep(x,duration_ms)



do = 523 #ド(523Hz)
re = 587 #レ(587Hz)
mi = 659 #ミ(659Hz)
fa = 698 #ファ(698Hz)
so = 784 #ソ(784Hz)
ra = 880 #ラ(880Hz)
si = 988 #シ(988Hz)
do2 = 1047 #ド(1047Hz)


pitchs = {}
pitchs["a"]  = do
pitchs["s"]  = re
pitchs["d"]  = mi
pitchs["f"]  = fa
pitchs["g"]  = so
pitchs["h"]  = ra
pitchs["j"]  = si
pitchs["k"]  = do2





while True:
    # 入力されたキーを認識する
    bytes_keyboard = getch()
    # バイト列から文字列に変換する
    str_keyboard = bytes_keyboard.decode("utf-8")
    # 文字列を小文字に揃える
    pitch = str_keyboard.lower()
    if pitch in pitchs:
        play_pitch(pitchs[pitch],duration_ms)
    # 終了させるときはqを押す
    elif pitch == 'q':
        break
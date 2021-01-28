import winsound  as ws #モジュールwsのインポート
import msvcrt as ms

duration_ms=300 #音の持続時間(ms) 

def play_pitch(x,y):
    win


do = ws.Beep(523, duration_ms) #ド(523Hz)
re = ws.Beep(587, duration_ms) #レ(587Hz)
mi = ws.Beep(659, duration_ms) #ミ(659Hz)
fa = ws.Beep(698, duration_ms) #ファ(698Hz)
so = ws.Beep(784, duration_ms) #ソ(784Hz)
ra = ws.Beep(880, duration_ms) #ラ(880Hz)
si = ws.Beep(988, duration_ms) #シ(988Hz)
do2 = ws.Beep(1047, duration_ms) #ド(1047Hz)


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
        play_pitch(pitchs[pitch], duration)
    # 終了させるときはqを押す
    elif pitch == 'q':
        break
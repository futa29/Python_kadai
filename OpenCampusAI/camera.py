# １．顔を探すための準備をします
import cv2
import aicommon
cascade = aicommon.initAI()

# ２．カメラの準備をします
cap = cv2.VideoCapture(0)

if cap.isOpened() is True:
        while True:
          # ３．カメラから画像を読み込みます
          ret,frame = cap.read()

          # ４．画像データから顔を探します
          face = cascade.detectMultiScale(frame)

          # ５．顔と判断した場所に枠を表示します
          if len(face) > 0:
                   for x,y,w,h in face:
                           cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
          cv2.imshow('camera',frame)




          # ６．Escキーが押されるとプログラムを終了させます
          if cv2.waitKey(1) == 27:
             break



cap.release()
cv2.destroyAllWindows()

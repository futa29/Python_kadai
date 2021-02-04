import cv2

try:
    path = 'C:\\Users\\184024\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\'

    cascade = cv2.CascadeClassifier(path+'haarcascade_frontalface_default.xml')

    img = cv2.imread('C:\\Users\\184024\\Desktop\\VSCode\\img\\hoge1.jpg',cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません')

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(gray,scaleFactor=1.5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255))


    cv2.imshow('face99 Tani Futa',img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)
    



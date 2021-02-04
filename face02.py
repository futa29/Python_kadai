import cv2

try:

    img = cv2.imread('C:\\Users\\184024\\Desktop\\VSCode\\img\\hoge1.jpg',cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません')

    cv2.imshow('face02-1 Tani Futa',img)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('face02-2 Tani Futa',gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


except FileNotFoundError as e:
    print(e)
import cv2

try:

    img = cv2.imread('C:\\Users\\184024\\Desktop\\VSCode\\img\\hoge1.jpg',cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError('ファイルが見つかりません')

    cv2.imshow('Original Tani Futa',img)

    dst1 = cv2.flip(img,0)
    cv2.imshow('Flip Upside Down Tani Futa',dst1)

    dst2 = cv2.flip(img,1)
    cv2.imshow('Flip horizontal Tani Futa',dst2)

    dst3 = cv2.flip(img,-1)
    cv2.imshow('Upside down left right reverse Tani Futa',dst3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(e)
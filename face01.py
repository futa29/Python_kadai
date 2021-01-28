import cv2

img = cv2.imread('C:\\Users\\184024\\Desktop\\VSCode\\img\\hoge1.jpg',cv2.IMREAD_COLOR)

cv2.imshow('face01',img)

cv2.waitKey(0)


cv2.destroyAllWindows()
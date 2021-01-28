import cv2

def initAI():
    xml_path = 'C:\\Users\\184024\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\'
    # xml_path = 'C:\\Users\\taiken\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\site-packages\\cv2\\data\\'
    xml_data = xml_path + 'haarcascade_frontalface_alt.xml'
    cascade = cv2.CascadeClassifier(xml_data)
    return cascade

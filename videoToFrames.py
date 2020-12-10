from cv2 import cv2
import numpy as np
import os

# video input initial 
cap = cv2.VideoCapture('sample.wmv')
isOpened = cap.isOpened()
# gain video stats
fps = cap.get(cv2.CAP_PROP_FPS)  
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  
print(fps, width, height)

# function defined
# extract frames and name them by even number
def changeToPics():
    i = 2
    while(isOpened):
        i = i + 2 
        flag, frame = cap.read()
        filename =  str(i) + '.png'
        if flag == True:
            cv2.imwrite(r'C:\Users\GTian\Desktop\Capstone\My solution\results' + os.sep + filename,frame)
            print(r'C:\Users\GTian\Desktop\Capstone\My solution' + os.sep + filename)
        else:
            print("Concert over")
            break
    print("convert successfully!!!")

# Function Execute
changeToPics()

from cv2 import cv2
import os
from datetime import datetime

# Function defined
def picToVideo(path, size):
    # path of the frame pitures
    filelist = os.listdir(path)  
    filelist.sort(key=lambda x: int(x[:-4]))  

    # the stats of the output video
    fps = 60
    file_path = r"./video" + "interpolation" + ".mp4"  

    #4-bit encoding for the decoder of the compressed frame
    fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')  

    video = cv2.VideoWriter(file_path, fourcc, fps, size)

    # find every .png file in the path 
    for item in filelist:
        if item.endswith('.png'):  
            item = path + '/' + item
            img = cv2.imread(item)  
            video.write(img)  
    # relese video
    video.release()  

picToVideo(r'./results', (1920, 1080))
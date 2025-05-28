import cv2
import numpy as np
import glob



def Video_Writing(image_path, video_name,fps):
    img_array = []
    for filename in glob.glob('{}/*.jpg'.format(image_path)):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)


    out = cv2.VideoWriter("{}.mp4".format(video_name),cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
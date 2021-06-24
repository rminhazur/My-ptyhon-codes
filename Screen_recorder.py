import datetime
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

time_stamp=datetime.datetime.now().strftime(" %Y-%m-%d   %H-%M-%S")
file_name=f'{time_stamp}.mp4'


fourcc= cv2.VideoWriter_fourcc("m","p","4","v")
cap_video=cv2.VideoWriter(file_name,fourcc,20.0, (width,height))

cam=cv2.VideoCapture(0)

while True:
    vid= ImageGrab.grab(bbox=(0,0,1920,1080))
    vid_np= np.array(vid)
    vid_final=cv2.cvtColor(vid_np,cv2.COLOR_BGR2RGB)
    _,  frame=cam.read()
    f_height, f_width, _= frame.shape
    vid_final[0: f_height, 0:f_width,:]=frame[0:f_height,0:f_width,:]


    cv2.imshow("Bokachoda Recorder",vid_final)
    #cv2.imshow("cam",frame)
    cap_video.write(vid_final)
    if cv2.waitKey(10)== ord("z"):
        break
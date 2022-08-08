# -*- coding: utf-8 -*-
from re import X
import pyautogui as pg
from PIL import ImageGrab
from functools import partial
import screeninfo
import time
import random

img_box = r'C:\python\image_processing\auto_lozzi\box.png'
img_more_box_g = r'C:\python\image_processing\auto_lozzi\more_box_g.png'
img_more_box = r'C:\python\image_processing\auto_lozzi\more_box.png'
img_gold_box = r'C:\python\image_processing\auto_lozzi\goldbox.png'
img_ok = r'C:\python\image_processing\auto_lozzi\ok.png'
img_x = r'C:\python\image_processing\auto_lozzi\x.png'
img_x2 = r'C:\python\image_processing\auto_lozzi\x2.png'
img_x3 = r'C:\python\image_processing\auto_lozzi\x3.png'
img_x4 = r'C:\python\image_processing\auto_lozzi\x4.png'
img_x5 = r'C:\python\image_processing\auto_lozzi\x5.png'
img_x6 = r'C:\python\image_processing\auto_lozzi\x6.png'
img_x7 = r'C:\python\image_processing\auto_lozzi\x7.png'
img_x8 = r'C:\python\image_processing\auto_lozzi\x8.png'
img_x9 = r'C:\python\image_processing\auto_lozzi\x9.png'
img_close = r'C:\python\image_processing\auto_lozzi\close.png'
img_control = r'C:\python\image_processing\auto_lozzi\control.png'
img_switch = r'C:\python\image_processing\auto_lozzi\switch.png'
#ImageGrab.grab(bbox=None, include_layered_windows=True)

tvwindow = pg.getWindowsWithTitle('Xiaomi_Mi A1_unknown - TeamViewer')
left_ = tvwindow[0].left + 100
top_ = tvwindow[0].top + 100
width_ = tvwindow[0].width
height_ = tvwindow[0].height
start_time = time.time()

def find_and_click(img):
    global start_time
    Flag = False
    b_random_click = False
    confi = 0.9
    left_random = 0
    left_top = 0

    if img == img_gold_box:
        config = 0.7  
 
    find_img = pg.locateOnScreen(img, confidence=confi, region=(left_, top_, width_, height_))
    
    if find_img != None:
        time.sleep(0.1)
        
        if img == img == img_more_box or img == img_more_box_g:
            find_img = (find_img.left + random.randrange(-5,5), find_img.top + random.randrange(-5,5), find_img.width, find_img.height)
            time.sleep(0.1)
        
        pg.click(find_img, clicks=1, duration=0.1)

        if img == img_box:
            pg.click(find_img, clicks=2, duration=0.1)

        #time.sleep(0.1)
        start_time = time.time()
        Flag = True

    return Flag


def make_switch():
    while True:
        time.sleep(0.2)

        if find_and_click(img_control):
            time.sleep(0.5)

            while True:
                time.sleep(0.2)
                if find_and_click(img_switch):
                    start_time = time.time()
                    return True


if __name__ =='__main__':
    try:
        while True:            
            
            find_and_click(img_box)
            find_and_click(img_more_box)
            find_and_click(img_more_box_g)
            find_and_click(img_gold_box)
            find_and_click(img_ok)
            find_and_click(img_x)
            find_and_click(img_x2)
            find_and_click(img_x3)
            find_and_click(img_x4)
            find_and_click(img_x5)
            find_and_click(img_x6)
            find_and_click(img_x7)
            find_and_click(img_x8)
            find_and_click(img_x9)
            find_and_click(img_close)

            if time.time() - start_time >= 30:
                make_switch()

            # 여기서 20초 넘으면 설정 클릭하고 홈 눌러서 강제로 더받기 박스 띄우기

    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass
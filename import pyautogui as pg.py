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
img_close = r'C:\python\image_processing\auto_lozzi\close.png'

#img_new = r'C:\Python3\work\image\new.png'

#ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
#ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
#ImageGrab.grab(bbox=None, include_layered_windows=True)
#find_img = pg.locateOnScreen(img_box, confidence=0.9) # 이미지가 있는 위치를 가져옵니다.
#find_img = pg.locateOnScreen(img_ok) # 이미지가 있는 위치를 가져옵니다.
#print(find_img)

#pg.moveTo(find_img)
#pg.click(find_img, clicks=1, duration=0.1)


#print(pg.position())

tvwindow = pg.getWindowsWithTitle('Xiaomi_Mi A1_unknown - TeamViewer')
left_ = tvwindow[0].left + 100
top_ = tvwindow[0].top + 100
width_ = tvwindow[0].width
height_ = tvwindow[0].height

def find_and_clik(img):
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
        Flag = True

    return Flag


if __name__ =='__main__':
    try:
        while True:            
            
            find_and_clik(img_box)
            find_and_clik(img_more_box)
            find_and_clik(img_more_box_g)
            find_and_clik(img_gold_box)            
            find_and_clik(img_ok)
            find_and_clik(img_x)
            find_and_clik(img_x2)
            find_and_clik(img_x3)
            find_and_clik(img_x4)
            find_and_clik(img_x5)
            find_and_clik(img_x6)
            find_and_clik(img_close)

    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass


'''
find_img = pg.locateOnScreen(img_box, confidence=0.9) # 이미지가 있는 위치를 가져옵니다.
if find_img != None:
    pg.click(find_img, clicks=1, duration=0.1)
    
find_img = pg.locateOnScreen(img_ok, confidence=0.9) # 이미지가 있는 위치를 가져옵니다.
if find_img != None:
    pg.click(find_img, clicks=1, duration=0.1)
'''



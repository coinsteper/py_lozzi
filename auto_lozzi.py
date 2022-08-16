# -*- coding: utf-8 -*-
import pyautogui as pg
from PIL import ImageGrab
from functools import partial
import screeninfo
import time
import random
import os

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
img_skip = r'C:\python\image_processing\auto_lozzi\skip.png'
img_skip1 = r'C:\python\image_processing\auto_lozzi\skip1.png'
img_close = r'C:\python\image_processing\auto_lozzi\close.png'

img_list = [img_box, img_more_box_g, img_more_box, img_gold_box, img_ok, img_x, img_x2, img_x3, img_x4, img_x5, img_x6, img_x7, img_x8,img_x9, img_skip, img_skip1
]

img_control = r'C:\python\image_processing\auto_lozzi\control.png'
img_switch = r'C:\python\image_processing\auto_lozzi\switch.png'
#ImageGrab.grab(bbox=None, include_layered_windows=True)

tvwindow = pg.getWindowsWithTitle('Xiaomi_Mi A1_unknown - TeamViewer')
left_g = tvwindow[0].left + 500
top_g = tvwindow[0].top + 200
width_g = tvwindow[0].width - 400
height_g = tvwindow[0].height - 100
start_time = time.time()

def find_and_click(img, pos=0):
    global start_time
    Flag = False
    b_random_click = False
    confi = 0.9
    left_random = 0
    left_top = 0

    top_ = top_g
    left_ = left_g
    width_ = width_g
    height_ = height_g

    if img == img_gold_box:
        config = 0.7   
 
    find_img = pg.locateOnScreen(img, confidence=confi, region=(left_, top_, width_, height_))

    if find_img != None:
        time.sleep(0.01)

        if img == img == img_more_box or img == img_more_box_g:
            find_img = (find_img.left + random.randrange(-5, 5), find_img.top + random.randrange(-5, 5), find_img.width,
                        find_img.height)
            time.sleep(0.01)

        pg.click(find_img, clicks=1, duration=0.1)

        if img == img_box:
            while True:
                find_img = pg.locateOnScreen(img, confidence=confi, region=(left_, top_, width_, height_))
                if find_img != None:
                    pg.click(find_img, clicks=2, duration=0.1)
                else:
                    break

        # time.sleep(0.1)
        start_time = time.time()
        Flag = True

    return Flag


def make_screenshot():
    timestr = time.strftime("%d-%H-%M")
    path = os.getcwd()
    filename = path + '\\screenshot\\' + timestr + '.png'
    print(filename)
    pg.screenshot(filename, region=(left_g, top_g, width_g-200, height_g-200))


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
            b_ret = find_and_click(img_gold_box)
            if b_ret:
                time.sleep(1)
                make_screenshot()            
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
            find_and_click(img_skip, 1)
            find_and_click(img_skip1, 1)            
            find_and_click(img_close, 3)

            '''
            for i in img_list:
                find_and_click(i)
            '''
            '''
            if time.time() - start_time >= 30:
                make_switch()
            '''
            # 여기서 20초 넘으면 설정 클릭하고 홈 눌러서 강제로 더받기 박스 띄우기

    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass
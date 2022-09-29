# -*- coding: utf-8 -*-
import pyautogui as pg
from PIL import ImageGrab
from functools import partial
import screeninfo
import time
import random
import os

img_box = r'C:\python\image_processing\auto_lozzi\img\box.png'
img_more_box_g = r'C:\python\image_processing\auto_lozzi\img\more_box_g.png'
img_more_box = r'C:\python\image_processing\auto_lozzi\img\more_box.png'
img_more_box2 = r'C:\python\image_processing\auto_lozzi\img\more_box2.png'
img_gold_box = r'C:\python\image_processing\auto_lozzi\img\goldbox.png'
img_gold_box_open = r'C:\python\image_processing\auto_lozzi\img\goldbox_open.png'
img_ok = r'C:\python\image_processing\auto_lozzi\img\ok.png'
img_ok2 = r'C:\python\image_processing\auto_lozzi\img\ok2.png'

#img_x = r'C:\python\image_processing\auto_lozzi\img\x.png'
#img_x2 = r'C:\python\image_processing\auto_lozzi\img\x2.png'
#img_x3 = r'C:\python\image_processing\auto_lozzi\img\x3.png'
#img_x4 = r'C:\python\image_processing\auto_lozzi\img\x4.png'
#img_x5 = r'C:\python\image_processing\auto_lozzi\img\x5.png'
#img_x6 = r'C:\python\image_processing\auto_lozzi\img\x6.png'
#img_x7 = r'C:\python\image_processing\auto_lozzi\img\x7.png'
#img_x8 = r'C:\python\image_processing\auto_lozzi\img\x8.png'
#img_x9 = r'C:\python\image_processing\auto_lozzi\img\x9.png'

img_path_x_list = r'C:\python\image_processing\auto_lozzi\img\x'
img_skip = r'C:\python\image_processing\auto_lozzi\img\skip.png'
img_skip1 = r'C:\python\image_processing\auto_lozzi\img\skip1.png'
img_close = r'C:\python\image_processing\auto_lozzi\img\close.png'
img_system = r'C:\python\image_processing\auto_lozzi\img\system.png'
img_goback = r'C:\python\image_processing\auto_lozzi\img\goback.png'
img_gosearch_google = r'C:\python\image_processing\auto_lozzi\img\search_google.png'
img_webb = r'C:\python\image_processing\auto_lozzi\img\webb.png'
img_control_in = r'C:\python\image_processing\auto_lozzi\img\control_in.png'

img_x_list = os.listdir(img_path_x_list)

img_control = r'C:\python\image_processing\auto_lozzi\img\control.png'
img_switch = r'C:\python\image_processing\auto_lozzi\img\switch.png'
#ImageGrab.grab(bbox=None, include_layered_windows=True)

tvwindow = pg.getWindowsWithTitle('BlueStacks App Player')
left_g = tvwindow[0].left + 440
top_g = tvwindow[0].top + 160
width_g = tvwindow[0].width - 150
height_g = tvwindow[0].height - 70
start_time = time.time()


def find_img(img, pos=0):
    global start_time
    Flag = False
    confi = 0.92
    
    top_ = top_g
    left_ = left_g
    width_ = width_g
    height_ = height_g

    find_img = pg.locateOnScreen(img, confidence=confi, region=(left_, top_, width_, height_))
    if find_img != None:
        Flag = True

    return Flag


def find_and_click(img, pos=0):
    global start_time
    Flag = False
    b_random_click = False
    confi = 0.92
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

        # 더 받기 랜덤한 좌표 클릭해서 봇체크 우회
        if img == img == img_more_box or img == img_more_box_g or img == img_more_box2:
            find_img = (find_img.left + random.randrange(-5, 5), find_img.top + random.randrange(-5, 5), find_img.width,
                        find_img.height)
            time.sleep(0.01)
        
        #x 잘못 클릭해서 링크로 빠지는거 방지
        if '_x_' in img:
            
            while True:
                time.sleep(1)
                find_img = pg.locateOnScreen(img, confidence=confi, region=(left_, top_, width_, height_))
                if find_img != None:
                    break

        pg.click(find_img, clicks=1, duration=0.1)
        #print(img)

        if img == img_box:
            while True:
                time.sleep(0.05)
                find_img = pg.locateOnScreen(img, confidence=confi, region=(left_, top_, width_, height_))
                if find_img != None:
                    pg.click(find_img, clicks=1, duration=0.1)
                else:
                    break

        # time.sleep(0.1)
        start_time = time.time()
        Flag = True

    #print(img)
    return Flag


def make_screenshot():
    timestr = time.strftime("%d-%H-%M")
    path = os.getcwd()
    filename = path + '\\screenshot\\' + timestr + '.png'
    print(filename)

    try:
        if not os.path.exists(path + '\\screenshot'):
            os.makedirs(path + '\\screenshot')

        start_time = time.time()    
        while True:
            img = pg.locateOnScreen(img_gold_box_open, confidence=0.9, region=(left_g, top_g, width_g, height_g))            
            if img:                
                ret = pg.screenshot(filename, region=(left_g, top_g, width_g-300, height_g-120))            
                break

            if time.time() - start_time >= 5:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)
   


def make_switch():
    start_time = time.time()

    while True:
        if time.time() - start_time >= 5:
            break

        time.sleep(0.2)

        if find_and_click(img_control):
            time.sleep(0.5)

            while True:
                if time.time() - start_time >= 5:
                    break

                time.sleep(0.2)
                if find_and_click(img_switch):
                    start_time = time.time()
                    return True


def go_back():
    confi = 0.92
    top_ = top_g
    left_ = left_g
    width_ = width_g
    height_ = height_g
    
    pg.click(x=tvwindow[0].left + 645, y=tvwindow[0].top + 336, clicks=1, duration=0.1)
    time.sleep(1)

    find_img = pg.locateOnScreen(img_goback, confidence=confi, region=(left_, top_, width_, height_))
    if find_img != None:
        pg.click(find_img, clicks=1, duration=0.1)


if __name__ =='__main__':
    try:
        while True:            
            find_and_click(img_box)
            find_and_click(img_more_box)
            find_and_click(img_more_box2)
            find_and_click(img_more_box_g)            
            b_ret = find_and_click(img_gold_box)
            if b_ret:
                time.sleep(0.2)
                make_screenshot()            
            find_and_click(img_ok)
            find_and_click(img_ok2)
            '''
            find_and_click(img_x)
            find_and_click(img_x2)
            find_and_click(img_x3)
            find_and_click(img_x4)
            find_and_click(img_x5)
            find_and_click(img_x6)
            find_and_click(img_x7)
            find_and_click(img_x8)
            find_and_click(img_x9)
            find_and_click(img_x11)
            '''

            # x는 동적으로 추가되더라도 잘 실행 되기 위해
            for i in img_x_list:
                find_and_click(img_path_x_list + '\\' + i, 1)

            #find_and_click(img_skip, 1)
            #find_and_click(img_skip1, 1)            
            find_and_click(img_close, 3)

            
            if find_img(img_gosearch_google) or find_img(img_control_in) or find_img(img_webb):
                go_back()

            '''
            for i in img_list:
                find_and_click(i)
            '''
            #print(time.time() - start_time)
            if time.time() - start_time >= 20:                
                make_switch()
                go_back()
                time.sleep(0.1)

            if time.time() - start_time >= 30:
                pass
            
            # 여기서 20초 넘으면 설정 클릭하고 홈 눌러서 강제로 더받기 박스 띄우기

    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass

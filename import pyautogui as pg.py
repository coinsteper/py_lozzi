# -*- coding: utf-8 -*-
import pyautogui as pg
from PIL import ImageGrab
from functools import partial
import screeninfo

img_path = r'C:\Python3\work\image\box.png'
img_more_box_g = r'C:\Python3\work\image\more_box_g.png'
img_ok = r'C:\Python3\work\image\ok.png'
#img_new = r'C:\Python3\work\image\new.png'

#ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
#ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
#ImageGrab.grab(bbox=None, include_layered_windows=True)
find_img = pg.locateOnScreen(img_path, confidence=0.9) # 이미지가 있는 위치를 가져옵니다.
#find_img = pg.locateOnScreen(img_ok) # 이미지가 있는 위치를 가져옵니다.
print(find_img)

#pg.moveTo(find_img)
pg.click(find_img, clicks=1, duration=0.1)
#pg.click(find_img, duration=0.1)

#print(pg.position())

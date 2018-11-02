from ctypes import*
import os,time
import pyautogui as pag
import win32con
import win32gui
from PIL import ImageGrab
#----------------------------

hwnd = win32gui.FindWindow("Shell_TrayWnd",None)
if not hwnd:
    print(RED,'window not found!',DEFAULT)
else:
    print(hwnd)

#win32gui.ShowWindow(hwnd,win32con.SW_RESTORE)       #强行显示界面
#win32gui.SetForegroundWindow(hwnd)      #将窗口提到最前
#截屏
game_rect = win32gui.GetWindowRect(hwnd)    #获取句柄矩形
src_image = ImageGrab.grab(game_rect)
src_image = ImageGrab.grab((game_rect[0]+116,game_rect[1]+390,game_rect[2]-117,game_rect[1]+747)) #截图句柄矩形
width,hight = src_image.size
#left_box = (0,0,476,hight)
#right_box = (571,0,width,hight)
#image_left = src_image.crop(left_box)
#image_right = src_image.crop(right_box)


#image_left.show()
#image_right.show()
#print(width,hight)

src_image.show()

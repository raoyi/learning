from PIL import ImageGrab
import win32gui
size = win32gui.GetWindowRect(win32gui.FindWindow("Shell_TrayWnd",None))

#sys-time coordinate
clockat = win32gui.GetWindowRect(0x0001013A)

#im = ImageGrab.grab()

#start coordinate, end coordinate
box = (size[0],size[1],clockat[0],size[3])
#im = im.crop(box)
im = ImageGrab.grab(box)
im.save('c:\\Users\\RaoYi\\Desktop\\test.png')

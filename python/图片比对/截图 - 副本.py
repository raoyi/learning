from PIL import ImageGrab
#im = ImageGrab.grab()

#开始点左，开始点上，结束点左，结束点上
box = (0, 728, 1246, 768)
#im = im.crop(box)
im = ImageGrab.grab(box)
im.save('c:\\Users\\RaoYi\\Desktop\\test.png')

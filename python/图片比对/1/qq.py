from PIL import Image
from PIL import ImageChops 

def compare_images(path_one, path_two, diff_save_location):

    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    try: 
        diff = ImageChops.difference(image_one, image_two)
 

        if diff.getbbox() is None:
        # 图片间没有任何不同则直接退出
            print("【+】图片一致")
        else:
            diff.save(diff_save_location)
    except ValueError as e:
        text = ("图片不一致")
        print("【{0}】{1}".format(e,text))

 
if __name__ == '__main__':
    compare_images('1.png',
                   '2.png',
                   'diff.png')

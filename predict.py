#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
import sys
import getopt
from yolo import YOLO
from PIL import Image

if (len(sys.argv) != 2):
    print('Usage: python predict.py <imagePath>')
    sys.exit(2)

yolo = YOLO()

try:
    image = Image.open(str(sys.argv[1]))
except:
    print('Open Error!')
    sys.exit(2)
else:
    r_image = yolo.detect_image(image)
    r_image.show()
    r_image.save('image_save_20200509.jpg')

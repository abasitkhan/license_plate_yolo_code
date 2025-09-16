# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
from time import time


# load the example image and convert it to grayscale
#image = cv2.imread("../croped/20.PNG",1)
image = cv2.imread("/home/humera/Desktop/vid02/72.png",1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur(gray, (5,5),0)
#gray = cv2.threshold(gray, 0, 255,
#		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#gray = cv2.bitwise_not(gray)
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
#filename= "{}.png".format(os.getpid())
#cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
#text = pytesseract.image_to_string(Image.open(filename))
t0 = time()
text = pytesseract.image_to_string((gray), lang='eng', 
        config='--psm 7')
t1 = time()

#print('function vers1 takes %f' %(t1-t0))

#os.remove(filename)
print('The license plate text::', text)

cv2.imshow("Window",gray)
cv2.waitKey()

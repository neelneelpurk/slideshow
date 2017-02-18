import numpy as np
import cv2
import imutils
import glob

print "Give your file location:"
string = str(raw_input())
images = glob.glob(string + '*.jpg')
ch_img = cv2.imread(images[0])
ch_img = imutils.resize(ch_img, width=340, height = 540)
for fn in images: 
	img = cv2.imread(fn)
	gray = imutils.resize(img, width=340, height = 540)

	for i in range(10) :
		j = i/(10.0)
		dst = cv2.addWeighted(gray,j,ch_img,(1-j),0)
		cv2.imshow('Slideshow',dst)
		if cv2.waitKey(150) & 0xFF == ord('q'):
        		break
	ch_img = cv2.imread(fn)
	ch_img = imutils.resize(ch_img, width=340, height = 540)

cv2.destroyAllWindows()

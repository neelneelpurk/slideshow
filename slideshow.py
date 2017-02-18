import numpy as np
import cv2
import imutils
import glob

images = glob.glob('*.jpg')
ch_img = cv2.imread('start.jpg')
ch_img = imutils.resize(ch_img, width=640, height = 540)
for fn in images: 
	img = cv2.imread(fn)
	gray = imutils.resize(img, width=640, height = 540)

	for i in range(10) :
		j = i/(10.0)
		dst = cv2.addWeighted(ch_img,j,gray,(1-j),0)
		cv2.imshow('Slideshow',dst)
		if cv2.waitKey(150) & 0xFF == ord('q'):
        		break

	ch_image = gray
cv2.destroyAllWindows()

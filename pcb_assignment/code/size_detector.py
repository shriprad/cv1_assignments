#Note: dpi is the pixel density or dots per inch.
#150 dpi means there are 150 pixels per inch.
#1 inch is equal to 2.54 centimeters.
# 1 inch = 2.54cm
#dpi = 150px/in
#150px/2.54cm
#1px = 2.54cm/150
#1px = 0.0169cm





import numpy as np
import math
import cv2

image = cv2.imread('pcb1000.png')



def calculate(img):



    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(imgray, (7,7), 0)
    edged = cv2.Canny(blur, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    ret, thresh = cv2.threshold(imgray, 127,255,cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img, contours,11, (0,255,0),2)
    cv2.drawContours(img, contours,12, (0,255,0),2)
    cv2.drawContours(img, contours,13, (0,255,0),2)
    cv2.drawContours(img, contours,23, (0,255,0),2)
    cv2.drawContours(img, contours,123, (0,255,0),2)
    cv2.drawContours(img, contours,128, (0,255,0),2)
    cv2.drawContours(img, contours,136, (0,255,0),2)


    for index,cnt in enumerate(contours):

        if index == 11 or index == 12 or index == 13 or index == 23 or index == 123 or index == 128 or index == 136:
            area_in_pixels = cv2.contourArea(cnt)

            radius_in_pixels= math.sqrt(area_in_pixels/math.pi)
            #So it says that every 1 px it is 0.0169 cm
            radius_in_cm = 0.0169 * radius_in_pixels

            print("Spacer Holes #{} has radius = {}".format(index,radius_in_cm))
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyALlWindows()


calculate(image)

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 08:40:18 2021

@author: Parth Malpathak
"""
#C:/Users/parth/OneDrive/Desktop//pcb.png
#C:/Users/parth/OneDrive/Desktop//golf.png
#C:/Users/parth/OneDrive/Desktop//pots.png
#C:/Users/parth/OneDrive/Desktop//rainbow.png
import cv2 as cv
import numpy as np

#Input Image
img1= input("Enter an Image for Smoothening and Sharpening process: ")
img = cv.imread(img1)
# =============================================================================
# scale_percent = 50
# 
# #calculate the 50 percent of original dimensions
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# 
# # dsize
# dsize = (width, height)
# img = cv.resize(img, dsize)
# =============================================================================


'''Smoothening'''

''''Blur Filter'''
blur = cv.blur(img, (5,5))

'''Box Blur'''
box = cv.boxFilter(img, -1, (3,3))

'''Bilateral FIlter'''
bilateral = cv.bilateralFilter(img, 10, 40,40)

'''Median FIlter'''
median = cv.medianBlur(img, 3) 
 
'''Gaussian Filter'''               
gaussian = cv.GaussianBlur(img, (7,7), 0)

'''Sharpening'''
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened = cv.filter2D(bilateral, -1, kernel)

'''Unsharp Masking'''
unsharped = cv.addWeighted(img, 1.5, gaussian, -0.5, 0)


#Display of All Images
cv.imshow("Original Image", img)
cv.imshow("Sharpened and Smoothened Image", sharpened)
#cv.imshow("Sharpened and Smoothened Image- Unsharped", unsharped)


cv.waitKey(0)
cv.destroyAllWindows()

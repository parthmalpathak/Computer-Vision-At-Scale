# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 23:18:15 2021

@author: Parth Malpathak
"""
#C:/Users/parth/OneDrive/Desktop//smiley.jpg
#C:/Users/parth/OneDrive/Desktop/CMU Lecture Files/CV for Engineers//carnival.jpg
import cv2
import numpy as np

img1 = input('Enter an image: ')    #Input Image
img = cv2.imread(img1)              #Read Image

print(img.shape)
g = float(input('Enter a gamma value: '))  #Enter the desired Gamma Value

def gamma_c(src, gamma):
    invGamma = 1.0 / g    #Gamma Inverse 
    #make a table to traverse over all pixel values, scale them to [0,1], apply gamma inverse
    #Scale it back to original
    t = np.array([(((i / 255.0) ** invGamma) * 255) for i in np.arange(0, 256)]).astype("uint8")
    print(t.shape)
    return cv2.LUT(img, t) #Create a look up table to link each pixel value to its corresponding gamma corrected value
scale_percent = 75 #Resize the image to fit the screen
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
original_resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('Carnival', original_resized) #Display Original Image

gammaImg = gamma_c(img, g ) 
scale_percent = 60 #Resize the image to fit the screen
width1 = int(gammaImg.shape[1] * scale_percent / 100)
height1 = int(gammaImg.shape[0] * scale_percent / 100)
dim = (width1, height1)

#resize image
original_resized_gamma = cv2.resize(gammaImg, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('Gamma corrected image', original_resized_gamma) #Display the gamma corrected image
cv2.waitKey(0)
cv2.destroyAllWindows()

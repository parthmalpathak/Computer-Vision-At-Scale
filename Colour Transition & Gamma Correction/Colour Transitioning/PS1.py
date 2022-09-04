# -*- coding: utf-8 -*-
#C:/Users/parth/OneDrive/Desktop/CMU Lecture Files/CV for Engineers/Homework 1//circuit.png
#C:/Users/parth/OneDrive/Desktop/CMU Lecture Files/CV for Engineers/Homework 1//crack.png
import cv2 as cv


test= input('Enter an image: ')   #Input an Image
#Ask the user if dark or bright side needs to be worked on
dbside= int(input("Do you want to convert brighter(Press 1) side or darker sider(Press 0): "))
img = cv.imread(test)
cv.imshow('Crack', img) #Show original Image
print(img.shape)
#Check the width and height for red image conversion
x= img.shape[0] 
y=img.shape[1]


#Convert and Display Image to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
cv.imshow('Crack_Grayscale', gray)

#Conver and Display Image to Binary
#Add max and min threshold to display a clear image
(thresh, blackAndWhiteImage) = cv.threshold(gray, 93, 255, cv.THRESH_BINARY) 
cv.imshow('Crack_Binary', blackAndWhiteImage)

#Convert Binary image to Blue Green and Red channel Image
Red_Image = cv.cvtColor(blackAndWhiteImage, cv.COLOR_BGR2RGB)
print(Red_Image)


for i in range (x): #Iterate through width
    for j in range (y): #Iterate through height
#If any pixel has colors other than black, convert them to red
        if (Red_Image[i][j]).any()== True and dbside == 1:
            Red_Image[i][j]= [0,0,255]
#If any pixel has black color, convert them to red       
        elif (Red_Image[i][j]).any()== False and dbside == 0:
            Red_Image[i][j]= [0,0,255]
#If any pixel has black color, convert them to the pixel color of the original image       
        elif (Red_Image[i][j]).any()== False and dbside == 1:
            Red_Image[i][j]= img[i][j]
#If any pixel has colors other than black, convert them to the pixel color of the original image       
        elif (Red_Image[i][j]).any()== True and dbside == 0:
            Red_Image[i][j]= img[i][j]    


cv.imshow('Crack_Red_Image', Red_Image) #Display Red Image

            
cv.waitKey(0)
cv.destroyAllWindows
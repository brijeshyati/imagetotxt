"""
reading the specific text from screenshot saving in png mode at the particular path(taken using selenium webdrive command)
for further details refer other script (screenshotUSINGseleniumwebdriver.py)

""""
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import cv2
import numpy as np
import pytesseract
from PIL import Image
from os import listdir
from os.path import isfile, join



# Path of working folder on Disk
orig_stdout = sys.stdout
f = open('C:\\Users\\XXXXXX\\python_learning\\LOG\\screenshottotxt_1.log', 'w')
sys.stdout = f
################


src_path = "C:/Users/XXXXXX/python_learning/pic/1/"
tt = src_path + "YYYYYY.png"
##print (tt)

def get_string(img_path,opt):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"), lang='eng', \
        config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')


    # Remove template file
    #os.remove(temp)
    print("1",result)
    #result = result.encode('ascii')
    #print("1",result)
    i = "Series ber tind"
    
    #print (i)
    if ( result == i):
        #print ("Failed")
        tt = print(opt.strip('.png'),"Failed",sep=',')
                   
    else :
        #print ("Not Match")
        tt = print(opt.strip('.png'),"Succesful",sep=',')
        
   return tt

def filesize():
    mypath ="C:/Users/XXXXXX/python_learning/pic/1/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    count=0
    fcount=0
    for opt in onlyfiles:
        fcount=len(onlyfiles)
        count +=1
        ff =mypath + opt
        #print(ff)
        print("------",count,"\\",fcount,"-------")
        get_string(ff,opt)
        

if __name__ == "__main__":
    print("=================================================================")
    print("--- Start recognize text from image ---")
    ##print(get_string(src_path + "YYYYYY.jpg") )
    filesize()
    print("------ script has been completed -------")
    print("=================================================================")

sys.stdout = orig_stdout
f.close()  
 
   

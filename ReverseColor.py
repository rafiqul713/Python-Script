import numpy as np
import cv2
import glob
import glob
import os.path
from os.path import basename
from skimage import util
from skimage.filter import threshold_otsu

from skimage import data
from skimage.feature import match_template
path=""
imageList=glob.glob(path+"*.tif")
print(imageList)

os.chdir(path)
for image in imageList:
    readImage = cv2.imread(image)
    imageName = os.path.basename(image)
    imageName = os.path.splitext(imageName)[0]
    Img=imageName
    print ("Now Extract from FROM NAME: " + imageName)

    # convert to Grayscale
    imageName = cv2.cvtColor(readImage, cv2.COLOR_BGR2GRAY)
    print(imageName)
    _, imageName = cv2.threshold(imageName, 170, 255, cv2.THRESH_BINARY)
    imageName = ~imageName
    print(imageName)
    cv2.imwrite(Img+"_"+".png",imageName)

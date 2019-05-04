import os
import glob

from PIL import Image
sourcePath=""
targetPath=""
os.chdir(sourcePath)
x=43
imageList=glob.glob("*.tif")
imageList=sorted(imageList)
for i in imageList:
    print(i)
    im = Image.open(i)
    im.save(targetPath+str(x)+'.png')
    x=x+1

import matplotlib
import matplotlib.pyplot as plt

from skimage.data import camera
from skimage.filter import threshold_otsu
from skimage import io
from skimage import color
from skimage import img_as_uint
matplotlib.rcParams['font.size'] = 9

sourcePath=""
targetPath=""

image = io.imread(sourcePath)
image=color.rgb2gray(image)
thresh = threshold_otsu(image)
binary = image > thresh
print(binary)
io.imsave(targetPath+"name.jpg",img_as_uint(binary))

#fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 2.5))
fig = plt.figure(figsize=(8, 2.5))
ax1 = plt.subplot(1, 3, 1, adjustable='box-forced')
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3, sharex=ax1, sharey=ax1, adjustable='box-forced')

ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Original')
ax1.axis('off')

ax2.hist(image)
ax2.set_title('Histogram')
ax2.axvline(thresh, color='r')

ax3.imshow(binary, cmap=plt.cm.gray)
ax3.set_title('Thresholded')
ax3.axis('off')

plt.show()
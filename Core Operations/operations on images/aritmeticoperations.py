# Image Addition 

'''
You can add two images with the OpenCV function, cv.add(), or simply by the numpy operation res = img1 + img2. 
Both images should be of same depth and type, or the second image can just be a scalar value.
'''
import cv2
import numpy as np
x = np.uint8([250])
y = np.uint8([10])
 
print( cv2.add(x,y) ) # 250+10 = 260 => 255

print( x+y )          # 250+10 = 260 % 256 = 4

# Image Blending

'''
This is also image addition, but different weights are given to images in order to give a feeling of blending or transparency.
Images are added as per the equation below:

g(x) = (1 - \alpha)f_{0}(x) + \alpha f_{1}(x)

By varying alpha from 0 to 1 you can perform a cool transition between one image to another.

Here I took two images to blend together. The first image is given a weight of 0.7 and the second image is given 0.3. 
cv.addWeighted() applies the following equation to the image:

dst = \alpha \cdot img1 + \beta \cdot img2 + \gamma

Here gamma is taken as zero.
'''

img1 = cv2.imread('ml.png')
img2 = cv2.imread('opencv-logo.png')
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"
 
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
 
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bitwise Operations

'''
This includes the bitwise AND, OR, NOT, and XOR operations. They will be highly useful while extracting any part of the image (as we will see in coming chapters), defining and working with non-rectangular ROI's, and etc. 
Below we will see an example of how to change a particular region of an image. I want to put the OpenCV logo above an image. If I add two images, it will change the color. If I blend them, I get a transparent effect. But I want it to be opaque. 
If it was a rectangular region, I could use ROI as we did in the last chapter. But the OpenCV logo is a not a rectangular shape. So you can do it with bitwise operations as shown below:
'''

# Load two images
img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo-white.png')
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"
 
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]
 
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
 
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
 
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
 
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
 
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
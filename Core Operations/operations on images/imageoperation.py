# Accessing and Modifying pixel values

import numpy as np
import cv2 as cv

img = cv.imread('messi5.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

px = img[100,100]
print( px )

# accessing only blue pixel
blue = img[100,100,0]
print( blue )

img[100,100] = [255,255,255]
print( img[100,100] )

# Accesing Image Properties

print( img.shape )

print( img.size )

print( img.size )

# Image ROI

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# Splitting and Merging Image Channels

b,g,r = cv.split(img)
img = cv.merge((b,g,r))

# Making Borders for Images (Padding)

'''
1. src - input image
2. top, bottom, left, right - border width in number of pixels in corresponding directions
3. borderType - Flag defining what kind of border to be added. It can be following types
    1. cv.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
    2. cv.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
    3. cv.BORDER_REFLECT_101 or cv.BORDER_DEFAULT - Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
    4. cv.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
    5. cv.BORDER_WRAP - Can't explain, it will look like this : cdefgh|abcdefgh|abcdefg
4. value - Color of border if border type is cv.BORDER_CONSTANT
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
 
BLUE = [255,0,0]
 
img1 = cv.imread('opencv-logo.png')
assert img1 is not None, "file could not be read, check with os.path.exists()"
 
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
 
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
 
plt.show()
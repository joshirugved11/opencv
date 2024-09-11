# Goal

'''
In image processing, since you are dealing with a large number of operations per second, it is mandatory that your code is not only providing the correct solution, but that it is also providing it in the fastest manner. 
So in this chapter, you will learn:

1. To measure the performance of your code.
2. Some tips to improve the performance of your code.
3. You will see these functions: cv.getTickCount, cv.getTickFrequency, etc.
'''

# Measuring Performance with OpenCV

'''
The cv.getTickCount function returns the number of clock-cycles after a reference event (like the moment the machine was switched ON) 
to the moment this function is called.
The cv.getTickFrequency function returns the frequency of clock-cycles, 
or the number of clock-cycles per second
'''

import cv2
e1 = cv2.getTickCount()
# your code execution
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()

img1 = cv2.imread('messi5.jpg')
assert img1 is not None, "file could not be read, check with os.path.exists()"
 
e1 = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print( t )
 
# Default Optimization in OpenCV

'''
ou can use cv.useOptimized() to check if it is enabled/disabled and cv.setUseOptimized() to enable/disable it. 
Let's see a simple example.
'''

# check if optimization is enabled
'''
In [5]: cv2.useOptimized()
Out[5]: True
 
In [6]: %timeit res = cv.medianBlur(img,49)
10 loops, best of 3: 34.9 ms per loop
'''
 
# Disable it
'''
In [7]: cv.setUseOptimized(False)
 
In [8]: cv.useOptimized()
Out[8]: False
 
In [9]: %timeit res = cv.medianBlur(img,49)
10 loops, best of 3: 64.1 ms per loop
'''

# Performance Optimization Techniques

'''
There are several techniques and coding methods to exploit maximum performance of Python and Numpy.

1. Avoid using loops in Python as much as possible, especially double/triple loops etc. They are inherently slow.
2. Vectorize the algorithm/code to the maximum extent possible, because Numpy and OpenCV are optimized for vector operations.
3. Exploit the cache coherence.
4. Never make copies of an array unless it is necessary. Try to use views instead. Array copying is a costly operation.
'''


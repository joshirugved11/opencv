# To put texts in images, you need specify following things.

'''
1. Text data that you want to write
2. Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
3. Font type (Check cv.putText() docs for supported fonts)
4. Font Scale (specifies the size of font)
5. regular things like color, thickness, lineType etc. For better look, lineType = cv.LINE_AA is recommended.
'''
import cv
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
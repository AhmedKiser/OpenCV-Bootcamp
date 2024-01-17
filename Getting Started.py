# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:27:11 2024

@author: User
"""

import cv2 #openCV use as cv2 in python
img1 = cv2.imread("Images/New_Zealand_Lake.jpg",1)
img1 = cv2.resize(img1, (700,700))
print(img1)
cv2.imshow("my image", img1)


img2 = cv2.imread("Images/New_Zealand_Lake.jpg",-1)
img2 = cv2.resize(img2, (700,700))
print(img2)
cv2.imshow("grayscale image", img2)



cv2.waitKey()
cv2.destroyAllWindows()


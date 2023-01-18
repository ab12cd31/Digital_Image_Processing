"""
File    : 3.3 代数运算.py
Date    : 2023.01.18
Author  : Simon Yang
Encoding： UTF-8
Software: PyCharm
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# 3.3.1 加法运算
Image1 = cv2.imread('../images/3.1.5.2.jpg')
Image2 = cv2.imread('../images/3.1.3.jpg')
Image_plus = cv2.add(Image1, Image2)
cv2.imshow('Image_plus', Image_plus)

# 3.3.2 减法运算
Image1 = cv2.imread('101.png')
Image2 = cv2.imread('102.png')
Image1 = cv2.resize(Image1, (1024, 768))
Image2 = cv2.resize(Image2, (1024, 768))
Image_minus1 = cv2.subtract(Image1, Image2)
Image_minus2 = Image1 - Image2
cv2.imshow('Image_minus1', Image_minus1)
cv2.imshow('Image_minus2', Image_minus2)

# 3.3.3 乘法运算
Image1 = cv2.imread('../DataSet/xueguanliu/train_img/1.png')
Image2 = cv2.imread('../DataSet/xueguanliu/train_mask/1.png')
Image1 = cv2.resize(Image1, (512, 512))
Image2 = cv2.resize(Image2, (512, 512))
Image_multiply = Image1*Image2
cv2.imshow('Image_multiply', Image_multiply)

# 图片展示延时
cv2.waitKey(0)
cv2.destroyAllWindows()

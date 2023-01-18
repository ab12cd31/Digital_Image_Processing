"""
File    : 3.2 直方图处理.py
Date    : 2023.01.16
Author  : Simon Yang
Encoding： UTF-8
Software: PyCharm
"""
import math
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 导入图片，重置尺寸
Image = cv2.imread('../images/3.1.4.jpg')
# Image = cv2.imread('181.png')
Image = cv2.resize(Image, (512, 512))
height = Image.shape[0]
width = Image.shape[1]
cv2.imshow('Image', Image)

# # 3.2.1 变成黑白图片
Image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Image_Gray', Image)

# 3.2.2 用opencv绘制直方图 单通道
plt.subplot(211)
# histb = cv2.calcHist([Image], [0], None, [256], [0, 255])
# histg = cv2.calcHist([Image], [1], None, [256], [0, 255])
histr = cv2.calcHist([Image], [0], None, [256], [0, 255])
# plt.plot(histb, color='b')
# plt.plot(histg, color='g')
plt.plot(histr, color='r')
# plt.yticks([])

# # 3.2.3 用plt画直方图
# plt.subplot(212)
# plt.xlim(0, 256)
# grayscale = plt.hist(Image.ravel(), 256)
# plt.yticks([])
# plt.show()

# 3.2.4 直方图均衡
Image_EqualizeHist = cv2.equalizeHist(Image)
cv2.imshow('Image_EqualizeHist',Image_EqualizeHist)
plt.subplot(212)
# histb = cv2.calcHist([Image_EqualizeHist], [0], None, [256], [0, 255])
# histg = cv2.calcHist([Image_EqualizeHist], [1], None, [256], [0, 255])
histr = cv2.calcHist([Image_EqualizeHist], [0], None, [256], [0, 255])
# plt.plot(histb, color='b')
# plt.plot(histg, color='g')
plt.plot(histr, color='r')
# plt.yticks([])

plt.show()
# 图片展示延时
cv2.waitKey(0)
cv2.destroyAllWindows()

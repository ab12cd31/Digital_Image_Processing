"""
File    : 3.1 灰度变换.py
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
Image = cv2.imread('1.tif')
Image = cv2.resize(Image, (512, 512))
height = Image.shape[0]
width = Image.shape[1]
# cv2.imshow('Image', Image)

# 3.1.1 变成黑白图片
Image_Gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Image_Gray', Image_Gray)
cv2.imwrite('../images/3.1.1.jpg', Image_Gray)

# 3.1.2 图像反转 Image Negatives
# 创建一幅空白图像
Image_Negatives = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        gray = 255 - Image_Gray[i, j]
        Image_Negatives[i, j] = np.uint8(gray)
# cv2.imshow('Image_Negatives', Image_Negatives)
cv2.imwrite('../images/3.1.2.jpg', Image_Negatives)

# 3.1.3 对数变换 Log Transformations
Image_Log = np.zeros((height, width), np.uint8)
c3 = 1
for i in range(height):
    for j in range(width):
        gray = c3 * math.log(1 + Image_Gray[i, j])
        Image_Log[i, j] = np.uint8(gray)
# cv2.imshow('Image_Log', Image_Log)
cv2.imwrite('../images/3.1.3.jpg', Image_Log)

# 3.1.4 幂次变换(伽马校正) Gamma Transformations ,有利于增加图像对比度
Image_Gamma = np.zeros((height, width), np.uint8)
c4 = 1
gamma = 0.8
for i in range(height):
    for j in range(width):
        gray = c4 * (Image_Gray[i, j] ** gamma)
        Image_Gamma[i, j] = np.uint8(gray)
cv2.imshow('Image_Gamma', Image_Gamma)
cv2.imwrite('../images/3.1.4.jpg', Image_Gamma)

# 3.1.5 分段线性变换 Piecewise Linear Transformation Functions
# 3.1.5.1 对比度拉伸 Contrast Stretching
Image_Contrast_Stretching = np.zeros((height, width), np.uint8)
r1, r2 = 94, 226
s1, s2 = 26, 154

for i in range(height):
    for j in range(width):
        if Image_Gray[i, j] <= r1:
            gray = (s1 / r1) * Image_Gray[i, j]
        elif r1 < Image_Gray[i, j] < r2:
            gray = ((s2 - s1) / (r2 - r1)) * Image_Gray[i, j] + s1
        else:
            gray = ((255 - s2) / (255 - r2)) * Image_Gray[i, j] + s2
        Image_Contrast_Stretching[i, j] = np.uint8(gray)
# cv2.imshow('Image_Contrast_Stretching', Image_Contrast_Stretching)
cv2.imwrite('../images/3.1.5.1.jpg', Image_Contrast_Stretching)

# 3.1.5.2 灰度级分层 Intensity-Level Slicing
Image_Intensity_Level_Slicing = np.zeros((height, width), np.uint8)
r1, r2 = 94, 226
s1, s2 = 26, 154

for i in range(height):
    for j in range(width):
        if Image_Gray[i, j] <= r1:
            gray = s1
        elif r1 < Image_Gray[i, j] < r2:
            gray = s2
        else:
            gray = s1
        Image_Intensity_Level_Slicing[i, j] = np.uint8(gray)
# cv2.imshow('Image_Intensity_Level_Slicing', Image_Intensity_Level_Slicing)
cv2.imwrite('../images/3.1.5.2.jpg', Image_Intensity_Level_Slicing)

# plt模块显示图片
plt.rcParams['font.sans-serif'] = 'KaiTi_GB2312'
plt.suptitle("Chap03 灰度变换", size=20, weight='bold')

Image_RGB = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
plt.subplot(241), plt.axis('off'), plt.title("1.原图", size=14), plt.imshow(Image_RGB)

plt.subplot(242), plt.axis('off'), plt.title("2.灰度变换", size=14), plt.imshow(Image_Gray, cmap='gray')

plt.subplot(243), plt.axis('off'), plt.title("3.图像反转", size=14), plt.imshow(Image_Negatives, cmap='gray')

plt.subplot(244), plt.axis('off'), plt.title("4.对数变换\nc={0}".format(c3), size=14), plt.imshow(Image_Log,
                                                                                                  cmap='gray')

plt.subplot(245), plt.axis('off'), plt.title("5.幂数变换\nc={0},gamma={1}".format(c4, gamma), size=14), plt.imshow(
    Image_Gamma, cmap='gray')

plt.subplot(246), plt.axis('off'), plt.title("6.对比度拉伸", size=14), plt.imshow(
    Image_Contrast_Stretching, cmap='gray')

plt.subplot(247), plt.axis('off'), plt.title("7.灰度级分层", size=14), plt.imshow(
    Image_Intensity_Level_Slicing, cmap='gray')

plt.savefig("../images/3.1.png", dpi=300)
plt.show()

# 图片展示延时
cv2.waitKey(0)
cv2.destroyAllWindows()

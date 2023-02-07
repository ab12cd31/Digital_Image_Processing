"""
File    : 3.6 高通（锐化）滤波器.py
Date    : 2023.02.06
Author  : Simon Yang
Encoding： UTF-8
Software: PyCharm
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

Image = cv2.imread("lena_gray_512.tif")
# cv2.imshow("Image", Image)
Image_blur = cv2.blur(Image, (3, 3))
cv2.imshow("Image_blur", Image_blur)

# # 3.6.1 锐化掩蔽
# Image_model = Image - Image_blur
# cv2.imshow("Image_model", Image_model)
#
# Image1 = Image + Image_model
# cv2.imshow("Image1", Image1)

# # 3.6.2 拉普拉斯锐化图像(以后换成自己设定核 不用预制函数了)(不可以检测边缘方向，但是能定位，对噪声敏感)
# kernel1 = np.array([[0, 1, 0],
#                     [1, -4, 1],
#                     [0, 1, 0]])
# Image2 = cv2.filter2D(Image_blur, -1, kernel=kernel1)
# cv2.imshow("Image2", Image2)
# Image3 = Image_blur - Image2
# cv2.imshow("Image3", Image3)
# kernel2 = np.array([[0, -1, 0],
#                     [-1, 4, -1],
#                     [0, -1, 0]])
# Image4 = cv2.filter2D(Image3, -1, kernel=kernel2)
# cv2.imshow("Image4", Image4)
# Image5 = Image3 + Image4
# cv2.imshow("Image5",Image5)

# 3.6.3 Robert算子（二阶,对噪声比较敏感）
kernel_Robert_X = np.array([[-1, 0],
                            [0, 1]])
kernel_Robert_Y = np.array([[0, -1],
                            [1, 0]])
Image_X = cv2.filter2D(Image_blur, -1, kernel=kernel_Robert_X)
Image_Y = cv2.filter2D(Image_blur, -1, kernel=kernel_Robert_Y)
Image6 = abs(Image_X) + abs(Image_Y)
cv2.imshow("Robert", Image6)

# 3.6.4 Prewitt算子
kernel_Prewitt_X = np.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]])
kernel_Prewitt_Y = np.array([[-1, -1, -1],
                             [0, 0, 0],
                             [1, 1, 1]])
Image_X = cv2.filter2D(Image_blur, -1, kernel=kernel_Prewitt_X)
Image_Y = cv2.filter2D(Image_blur, -1, kernel=kernel_Prewitt_Y)
Image7 = abs(Image_X) + abs(Image_Y)
cv2.imshow("Prewitt", Image7)

# 3.6.5 Sobel算子(可以检测边缘方向，但是不能定位，对噪声较不敏感)
kernel_Sobel_X = np.array([[-1, -2, -1],
                           [0, 0, 0],
                           [1, 2, 1]])
kernel_Sobel_Y = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])
Image_X = cv2.filter2D(Image_blur, -1, kernel=kernel_Sobel_X)
Image_Y = cv2.filter2D(Image_blur, -1, kernel=kernel_Sobel_Y)
Image8 = abs(Image_X) + abs(Image_Y)
cv2.imshow("Sobel", Image8)

# 图片展示延时
cv2.waitKey(0)
cv2.destroyAllWindows()

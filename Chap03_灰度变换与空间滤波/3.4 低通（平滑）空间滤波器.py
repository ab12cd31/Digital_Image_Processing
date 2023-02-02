"""
File    : 3.4 低通（平滑）空间滤波器.py
Date    : 2023.01.31
Author  : Simon Yang
Encoding： UTF-8
Software: PyCharm
"""
import random
import cv2
import matplotlib.pyplot as plt
import numpy as np

Image = cv2.imread("lena_gray_512.tif")
cv2.imshow("lena_gray_Default", Image)


# 前置工作 加椒盐噪声和高斯噪声
def sp_noise(image, prob):
    # prob means probability of the white noise in one of the pixel in the image
    # thres means prob of the black noise in image
    # in fact thres = 1 - prob , they are symmetric
    thres = 1 - prob
    output = np.zeros(image.shape, np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            x = random.random()
            if x < prob:
                output[i][j] = 0
            elif x > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def gaussian_noise(image, mean=0, var=0.001):
    image = np.array(image / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)  # 正态分布
    output = image + noise
    if output.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    output = np.clip(output, low_clip, 1.0)
    output = np.uint8(output * 255)
    return output


Image_sp_noise = sp_noise(Image, 0.01)
Image_gasuss_noise = gaussian_noise(Image, mean=0, var=0.01)
cv2.imshow("Image_sp_noise", Image_sp_noise)
cv2.imshow("Image_gasuss_noise", Image_gasuss_noise)
cv2.imwrite('../images/3.4 Image_gasuss_noise.jpg', Image_gasuss_noise)

# 3.4.1.1 3*3均值滤波器 box kernels of sizes 3*3
Image1 = cv2.blur(Image_sp_noise, (3, 3))
cv2.imshow("box kernels of sizes 3*3", Image1)
cv2.imwrite('../images/3.4.1.1 kernels sizes 3.jpg', Image1)

# 3.4.1.2 5*5均值滤波器 box kernels of sizes 5*5
Image2 = cv2.blur(Image_sp_noise, (5, 5))
cv2.imshow("box kernels of sizes 5*5", Image2)
cv2.imwrite('../images/3.4.1.2 kernels sizes 5.jpg', Image2)

# 3.4.1.3 10*10均值滤波器 box kernels of sizes 10*10
Image3 = cv2.blur(Image_sp_noise, (10, 10))
cv2.imshow("box kernels of sizes 10*10", Image3)
cv2.imwrite('../images/3.4.1.3 kernels sizes 10.jpg', Image3)

# 3.4.2.1 低通高斯滤波 Lowpass filtering with a Gaussian kernel
Image4 = cv2.GaussianBlur(Image_sp_noise, (5, 5), 1)
cv2.imshow("Gaussian kernel sizes 5*5", Image4)
cv2.imwrite('../images/3.4.2.1 kernels sizes 5.jpg', Image4)

# 3.4.2.2 低通高斯滤波 Lowpass filtering with a Gaussian kernel
Image5 = cv2.GaussianBlur(Image_gasuss_noise, (5, 5), 1)
cv2.imshow("Gaussian kernel sizes 5*5(gaussian)", Image5)
cv2.imwrite('../images/3.4.2.2 kernels sizes 5.jpg', Image5)

# 图片展示延时
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
File    : 3.5 带通（中值）滤波器.py
Date    : 2023.02.04
Author  : Simon Yang
Encoding： UTF-8
Software: PyCharm
"""
import cv2
import matplotlib.pyplot as plt

Image = cv2.imread("../images/3.4 Image_noise.jpg")
Image_blur = cv2.imread("../images/3.4.1.2 kernels sizes 5.jpg")
cv2.imshow("Image_noise", Image)

# 3.5.1 中值滤波
Image_median = cv2.medianBlur(Image, 5)
cv2.imshow("Image_medianblur",Image_median)
cv2.imwrite('../images/3.5.1 medainBlur.jpg', Image_median)

plt.suptitle("3.5 Median_Blur and default blur", size=20)
plt.subplot(131),plt.axis('off'), plt.title("Default", size=14), plt.imshow(Image)
plt.subplot(132),plt.axis('off'), plt.title("Default Blur", size=14), plt.imshow(Image_blur)
plt.subplot(133),plt.axis('off'), plt.title("Median Blur", size=14), plt.imshow(Image_median)
plt.savefig("../images/3.5.png", dpi=300)
plt.show()

# 图片展示延时
cv2.waitKey(0)
cv2.destroyAllWindows()
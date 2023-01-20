# OpenCV, ознакомление и тестовая работа

import cv2

image = cv2.imread("opencv/pic.jpg")
print(image.shape)
image = cv2.resize(image, (500, 500))
print(image.shape)

cv2.imshow("Result", image)

cv2.waitKey()
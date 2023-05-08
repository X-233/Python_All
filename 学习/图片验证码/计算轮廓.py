import cv2
import numpy as np

def sab():
    # 读取图像
    img = cv2.imread('tu1.png', cv2.IMREAD_GRAYSCALE)

    # 计算Sobel算子
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    # 计算梯度幅值和方向
    grad = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    grad = np.uint8(grad)
    theta = np.arctan2(sobel_y, sobel_x)

    # 显示图像
    cv2.imshow('Image', img)
    cv2.imshow('Sobel X', np.uint8(np.absolute(sobel_x)))
    cv2.imshow('Sobel Y', np.uint8(np.absolute(sobel_y)))
    cv2.imshow('Gradient', grad)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def canny(img_1):
    # 读取图像
    img = cv2.imread(img_1, cv2.IMREAD_GRAYSCALE)

    # 对图像进行二值化处理
    ret, thresh = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)

    # 对图像进行边缘检测
    # edges = cv2.Canny(thresh, 250, 255)

    # 显示图像
    # cv2.imshow('Image', img)
    # cv2.imshow('Threshold', thresh)
    # cv2.imshow('Edges', edges)
    cv2.imwrite('..\\图片验证码\\' + '_' + img_1, thresh)


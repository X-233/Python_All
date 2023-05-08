import cv2

# 读取图片1和图片2
img1 = cv2.imread('tu1.png')
img2 = cv2.imread('tu2.png')

# 打印图像形状
print("img1的形状：", img1.shape)
print("img2的形状：", img2.shape)

# 将图片转换为灰度图像
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 计算差异图
diff = cv2.absdiff(gray1, gray2)

# 对差异图进行二值化处理
thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]

# 查找轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 计算最大轮廓
max_contour = max(contours, key=cv2.contourArea)

# 计算轮廓的外接矩形
x, y, w, h = cv2.boundingRect(max_contour)

# 计算中心坐标
center_x = x + w // 2
center_y = y + h // 2

print("缺口中心坐标：({}, {})".format(center_x, center_y))

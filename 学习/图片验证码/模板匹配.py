import cv2

def pipei():
    # 读取两张图片
    img1 = cv2.imread('_tu2.png', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('_tu1.png', cv2.IMREAD_GRAYSCALE)

    print("================================")

    # 在img2中查找img1
    result = cv2.matchTemplate(img2, img1, cv2.TM_CCOEFF_NORMED)

    # 获取img1的尺寸
    h, w = img1.shape[:2]

    # 找到最大匹配值的位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 计算匹配位置的左上角坐标和右下角坐标
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 在img2中画出匹配结果
    cv2.rectangle(img2, top_left, bottom_right, 255, 2)

    print(top_left)
    print(bottom_right)
    return (top_left[0] + bottom_right[0]) / 2
    # # 显示匹配结果
    # cv2.imshow('Match Result', img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


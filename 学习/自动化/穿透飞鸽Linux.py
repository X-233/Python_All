import base64
from time import sleep
from selenium.webdriver import ChromeOptions, ActionChains, Chrome
from selenium.webdriver.common.by import By
# from 学习.图片验证码.打码平台 import base64_api
import cv2

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
    cv2.imwrite('_' + img_1, thresh)

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

if __name__ == '__main__':
    # 添加参数
    options = ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument('--headless')  # 浏览器不提供可视化页面.linux下如果系统不支持可视化不加这条会启动失败

    # 创建对象
    web = Chrome(options=options)
    web.get('https://fgnwct.com/login.html')
    # web.maximize_window()
    #隐式等待
    web.implicitly_wait(10)

    # 找到元素
    web.find_element(By.CSS_SELECTOR, '#email').send_keys('1972125164@qq.com')
    web.find_element(By.CSS_SELECTOR, '#password').send_keys('zhanglin')
    web.find_element(By.CSS_SELECTOR, '.form-control.btn.btn-primary').click()

    sleep(2)
    web.find_element(By.ID, 'btn').click()
    sleep(2)
    # base64_data_4 = web.find_element('xpath', '//title').text
    # print(base64_data_4)
    base64_data = web.find_element(By.CSS_SELECTOR, 'div.verifybox div.verify-img-out img').get_attribute('src')
    base64_data_1 = web.find_element(By.CSS_SELECTOR, '.verify-sub-block img').get_attribute('src')

    base64_data = base64_data.split(',')[-1]
    base64_data_1 = base64_data_1.split(',')[-1]
    data_1 = base64.b64decode(base64_data)
    data_2 = base64.b64decode(base64_data_1)
    with open('tu1.png', 'wb')as f:
        f.write(data_1)
    with open('tu2.png', 'wb')as f:
        f.write(data_2)

    select_1 = web.find_element(By.CSS_SELECTOR, 'div.verify-img-out')
    select_1.screenshot('tu3.png')

    sleep(2)
    # x = int(base64_api(img=['tu3.png'], typeid=33))
    canny('tu1.png')
    canny('tu2.png')
    x = pipei()
    print(x)
    action = web.find_element(By.CSS_SELECTOR, 'div.verify-move-block')
    action_1 = ActionChains(web)
    # # 移动鼠标到元素上
    # action_1.move_to_element(action)
    # # 然后通过循环来逐步移动鼠标
    # steps = 5  # 设定需要移动的步数
    # for j in range(steps+1):
    #     # 计算当前需要移动的距离
    #     x_1 = j * x / steps
    #     y_1 = 0
    #     # sleep(random.random())
    #     # 将鼠标移动到新的位置
    #     action_1.move_by_offset(x_1, y_1)
    action_1.drag_and_drop_by_offset(action, x-46, 0).perform()

    sleep(5)
    web.quit()






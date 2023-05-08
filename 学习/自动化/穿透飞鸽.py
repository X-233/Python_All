import base64
from time import sleep
from selenium.webdriver import ChromeOptions, ActionChains, Chrome
from selenium.webdriver.common.by import By
# from 学习.图片验证码.打码平台 import base64_api
from 学习.图片验证码.计算轮廓 import canny
from 学习.图片验证码.模板匹配 import pipei

if __name__ == '__main__':
    # 添加参数
    options = ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument('--headless')  # 浏览器不提供可视化页面.linux下如果系统不支持可视化不加这条会启动失败

    # 创建对象
    web = Chrome(options=options)
    web.get('https://fgnwct.com/login.html')
    web.maximize_window()
    #隐式等待
    web.implicitly_wait(10)

    # 找到元素
    web.find_element(By.CSS_SELECTOR, '#email').send_keys('1972125164@qq.com')
    web.find_element(By.CSS_SELECTOR, '#password').send_keys('zhanglin')
    web.find_element(By.CSS_SELECTOR, '.form-control.btn.btn-primary').click()

    sleep(2)
    web.find_element(By.ID, 'btn').click()
    sleep(2)
    base64_data = web.find_element(By.CSS_SELECTOR, 'div.verifybox div.verify-img-out img').get_attribute('src')
    base64_data_1 = web.find_element(By.CSS_SELECTOR, '.verify-sub-block img').get_attribute('src')
    base64_data = base64_data.split(',')[-1]
    base64_data_1 = base64_data_1.split(',')[-1]
    data_1 = base64.b64decode(base64_data)
    data_2 = base64.b64decode(base64_data_1)
    with open('..\\图片验证码\\tu1.png', 'wb')as f:
        f.write(data_1)
    with open('..\\图片验证码\\tu2.png', 'wb')as f:
        f.write(data_2)

    select_1 = web.find_element(By.CSS_SELECTOR, 'div.verify-img-out')
    select_1.screenshot('..\\图片验证码\\tu3.png')

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






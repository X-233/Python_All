from time import sleep

from selenium.webdriver import ChromeOptions, Chrome, ActionChains
from selenium.webdriver.common.by import By
import threading

def dump_1(ele):
    while True:
        if ele.find_element(By.CSS_SELECTOR, '#login-pannel'):
            ele.find_element(By.CSS_SELECTOR, '#login-pannel div.dy-account-close').click()
        else:
            ele.find_element(By.CSS_SELECTOR, 'input.igFQqPKs.qYYUxsS2').send_keys('动漫')
            ele.find_element(By.CSS_SELECTOR, 'button.rB8dMXOc').click()
            break
    sleep(5)

if __name__ == '__main__':
    option = ChromeOptions()

    option.add_argument('--disable-blink-features=AutomationControlled')

    web = Chrome(options=option)

    web.get('https://www.douyin.com/')
    web.maximize_window()
    web.implicitly_wait(time_to_wait=10)

    # threading.Thread(target=dump_1, args=(web, ))
    if web.find_element(By.CSS_SELECTOR, '#login-pannel'):
        web.find_element(By.CSS_SELECTOR, '#login-pannel div.dy-account-close').click()
    web.find_element(By.CSS_SELECTOR, 'input.igFQqPKs.qYYUxsS2').send_keys('动漫')
    web.find_element(By.CSS_SELECTOR, 'button.rB8dMXOc').click()

    web.switch_to.window(web.window_handles[-1])
    page = web.page_source
    with open('1.html', 'w', encoding='utf-8') as f:
        f.write(page)

    input()

import random
import re

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
#键盘操作
from selenium.webdriver.common.keys import Keys
from time import sleep
#下拉select,css动态加载出来的
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import parsel
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = [
    'https://xiaomeiwu.tmall.com/search.htm?spm=a1z10.1-b-s.0.0.76f64e98EOh11W&search=y',
    'https://jiahuafood.tmall.com/search.htm?spm=a1z10.1-b-s.w5001-24284525272.4.653a52d7LGPgkG&search=y',
    'https://keyueshipin.tmall.com/search.htm?spm=a1z10.1-b.0.0.406968a78V4zms&search=y',
    'https://chaogesp.tmall.com/search.htm?spm=a1z10.1-b.w5001-18689864076.3.22a16cb70dHo7k&search=y',
    'https://keewahbakery.tmall.com/search.htm?spm=a1z10.1-b-s.w20166435-22999678872.2.322428efCpKp4t&search=y',
    'https://lakexixi.tmall.com/search.htm?spm=a1z10.1-b-s.w5002-24618197582.1.bdca6b8cEqIelC&search=y',
]
url_1 = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua.754894437.1.11a911d9YotdBE&f=top&redirectURL=http%3A%2F%2Ftb.alicdn.com%2Fsnapshot%2Findex.html'

class Login_Tao:
    def __init__(self):
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.web = Chrome(options=options)
        self.web.maximize_window()
        self.cookie = None
        self.cookies = None

    def login(self):
        self.web.get(url=url_1)

        self.login_1()
        self.tuo_hua_kuai_1()
        self.web.switch_to.default_content()

        sleep(2)
        self.cookie = self.web.get_cookies()
        self.cookie_s()
        print(self.cookies)
        # self.web.add_cookie(self.cookies)
        sleep(1)

    def tuo_hua_kuai(self):
        try:
            self.set_xy()
        except Exception as e:
            # print(e)
            pass

    def tuo_hua_kuai_1(self):
        try:
            self.set_xy()
            sleep(1)
        except Exception as e:
            # print(e)
            pass

    def login_1(self):
        sleep(2)
        self.web.find_element(By.XPATH, '//input[@id="fm-login-id"]').send_keys('17684106197')
        sleep(0.5)
        self.web.find_element(By.XPATH, '//input[@id="fm-login-password"]').send_keys('zhanglin0619')
        sleep(0.3)
        self.web.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/button').click()
        sleep(2)

    def set_xy(self):
        while True:
            sleep(1)
            self.web.switch_to.frame('baxia-dialog-content')
            sleep(0.5)
            ele = self.web.find_element(By.XPATH, '//span[@id="nc_1_n1z"]')
            ele_1 = self.web.find_element(By.XPATH, '//*[@id="nc_1__scale_text"]/span')
            # 假设web是一个WebDriver对象，element是一个可拖动的元素，x_offset和y_offset是需要移动的距离
            # 首先创建一个ActionChains对象
            try:
                sleep(1)
                self.web.find_element(By.XPATH, '//*[@id="J_SiteNavLogin"]')
                print('登陆成功！')
                break
            except Exception as e:
                print('还没登陆成功')
            actions = ActionChains(self.web)
            # 移动鼠标到元素上
            actions.move_to_element(ele)

            # 然后通过循环来逐步移动鼠标
            steps = 8  # 设定需要移动的步数
            for j in range(3):
                # 计算当前需要移动的距离
                x = j * 300 / steps + random.random()
                y = j * 30 / steps + random.random()
                # sleep(random.random())
                # 将鼠标移动到新的位置
                actions.move_by_offset(x, y)

            sleep(3)
            # 最后执行拖放操作
            actions.drag_and_drop_by_offset(ele, 300, 20).perform()
            sleep(2)
            # actions.drag_and_drop_by_offset(element, 320, 40).perform()

    def set_xy_1(self):

            try:
                ele = self.web.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
                ele_1 = self.web.find_element(By.XPATH, '//*[@id="nc_1__scale_text"]/span')
                actions = ActionChains(self.web)
                # 移动鼠标到元素上
                actions.move_to_element(ele)
                sleep(1)
                # 最后执行拖放操作
                actions.drag_and_drop_by_offset(ele, ele_1.size['width'], ele_1.size['height']).perform()
                sleep(1)
                lo.web.refresh()
                # actions.drag_and_drop_by_offset(element, 320, 40).perform()
            except:
                pass

    def cookie_s(self):
        # self.cookies = {i.split('=')[0]: i.split('=')[-1] for i in self.cookie['cookie'].split('; ')}
        self.cookies = "; ".join([item["name"] + "=" + item["value"] for item in self.web.get_cookies()])


if __name__ == '__main__':
    lo = Login_Tao()
    lo.login()
    sleep(2)
    data_list = []
    for i in url:
        lo.web.get(i)
        sleep(2)
        lo.web.refresh()
        sleep(2)
        lo.set_xy_1()
        sleep(3)
        # 滑动到最底部
        js_button = 'document.documentElement.scrollTop=10000'
        # 执行js，滑动到最底部
        lo.web.execute_script(js_button)
        sleep(20)
        # WebDriverWait(lo.web, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="banner-box"]/img')))
        pag_so = lo.web.page_source
        # with open('1.txt', 'w', encoding='utf-8') as file:
        #     file.write(pag_so)
        select_1 = parsel.Selector(pag_so)
        x_data = select_1.xpath('//div[@class="J_TItems"]/div[@class="item5line1"]')
        print(select_1.xpath('//head/meta[@name="keywords"]/@content').get())
        title = select_1.xpath('//head/meta[@name="keywords"]/@content').get()
        title_img = 'https://gdp.alicdn.com/' + re.findall('//gdp\.alicdn\.com/(.*?)\.png', pag_so, re.S)[0] + '.png'
        print(title_img)
        if len(title_img) > 100:
            title_img = 'https://gdp.alicdn.com/' + re.findall('//gdp\.alicdn\.com/(.*?)\.jpg', title_img, re.S)[0] + '.jpg'
        data_list_1 = []
        num_1 = 1
        for k in x_data:
            for v in k.xpath('./dl'):
                img_alt = v.xpath('.//img/@alt').get()
                img_url = 'https:' + v.xpath('.//img/@src').get()
                if 's.gif' in img_url:
                    img_url = 'https:' + v.xpath('.//img/@data-ks-lazyload').get()
                img_url = img_url.replace('180x180', '360x360')
                symbol = v.xpath('.//span[@class="symbol"]/text()').get()
                price = symbol + v.xpath('.//span[@class="c-price"]/text()').get()
                # sale_num = v.xpath('.//span[@class="sale-num"]/text()').get()
                data_dict = {
                    'img_alt': img_alt,
                    'img_url': img_url,
                    'price': str(price),
                    # 'sale_num': str(sale_num),
                }
                data_list_1.append(data_dict)
        data_list.append({'Title': title, 'title_img': title_img, 'data': data_list_1})
        sleep(4)
    lo.web.quit()
    with open('data.json', 'w', encoding='utf-8') as f:
        f.write(str(data_list))

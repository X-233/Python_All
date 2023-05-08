from selenium.webdriver import Chrome, ActionChains, ChromeOptions

option = ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')

web = Chrome(options=option)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def configurar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    return browser

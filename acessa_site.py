from selenium.webdriver.common.keys import Keys
from conf_driver import configurar_driver

browser = configurar_driver()

browser.get("https://www.magazineluiza.com.br/")

pesquisar = browser.find_element_by_id('input-search')
pesquisar.send_keys("Notebook")
pesquisar.send_keys(Keys.ENTER)
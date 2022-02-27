from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from conf_driver import configurar_driver

browser = configurar_driver()

browser.get("https://www.magazineluiza.com.br/")

pesquisar = browser.find_element_by_id('input-search')
pesquisar.send_keys("Notebook")
pesquisar.send_keys(Keys.ENTER)
sleep(10)


browser.find_element_by_css_selector("#__next > div > main > div > div.sc-eCImPb.bnqaGh > button").click()
proximo = browser.find_element_by_css_selector("#__next > div > main > section:nth-child(5) > div.sc-GEbAx.kCOyTU > nav > ul > li:nth-child(9) > button")

nome_note = []
preco_note = []
while proximo:
    browser.find_element_by_css_selector("#__next > div > main > section:nth-child(5)")
    browser.find_element_by_css_selector("#__next > div > main > section:nth-child(5) > div.sc-GEbAx.fqFzsY")
    browser.find_element_by_css_selector("#__next > div > main > section:nth-child(5) > div.sc-GEbAx.fqFzsY > div")
    ul_notes = browser.find_element_by_css_selector("#__next > div > main > section:nth-child(5) > div.sc-GEbAx.fqFzsY > div > ul")
    lista_note = ul_notes.find_elements_by_tag_name("li")
    
    for l in lista_note:
        try:
            sem_estoque = l.find_element_by_css_selector("#__next > div > main > section:nth-child(5) > div.sc-GEbAx.fqFzsY > div > ul > li:nth-child(59) > a > div.sc-cnTVOG.ICkyN > div.sc-gsFzgR.fHDydZ > span > font > font").text
            print(sem_estoque)
        except NoSuchElementException:
            produto = l.find_element_by_tag_name("h2").text
            precos = l.find_elements_by_tag_name("p")
            for p in precos:
                preco = precos[1].text
            print(produto)
            print(preco)
            nome_note.append(produto)
            preco_note.append(preco)
           
        
    proximo.click()
    #sleep(10)
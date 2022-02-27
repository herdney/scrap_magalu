import pandas as pd
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from conf_driver import configurar_driver
from lista_dataf import criar_dataframe

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

browser.find_element_by_css_selector("#__next > div > main > section:nth-child(5)")
browser.find_element_by_css_selector("#__next > div > main > section:nth-child(5) > div.sc-GEbAx.fqFzsY")
browser.find_element_by_css_selector("#__next > div > main > section:nth-child(5) > div.sc-GEbAx.fqFzsY > div")
ul_notes = browser.find_element_by_css_selector("#__next > div > main > section:nth-child(5) > div.sc-GEbAx.fqFzsY > div > ul")
lista_note = ul_notes.find_elements_by_tag_name("li")

for l in lista_note:
    try:
        sem_estoque = l.find_element_by_css_selector("#__next > div > main > section:nth-child(5) > div.sc-GEbAx.fqFzsY > div > ul > li:nth-child(59) > a > div.sc-cnTVOG.ICkyN > div.sc-gsFzgR.fHDydZ > span > font > font").text
    except NoSuchElementException:
        produto = l.find_element_by_tag_name("h2").text
        precos = l.find_elements_by_tag_name("p")
        qtde_p = len(precos)
        if qtde_p ==3:
            for p in precos:
                preco = precos[1].text
        else:
            for p in precos:
                preco = precos[0].text
        nome_note.append(produto)
        preco_note.append(preco)
        print(produto, preco)

browser.quit()

lista_produtos = criar_dataframe(nome_note, preco_note)
writer = pd.ExcelWriter("Preços Notebook.xlsx", engine='xlsxwriter')
lista_produtos.to_excel(writer,sheet_name = "notebooks", index=False)
writer.save() 
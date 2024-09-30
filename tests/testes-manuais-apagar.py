from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep


chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--log-level=3")
# chrome_options.add_argument("--headless")

url = "https://www.kabum.com.br/celular-smartphone/smartphones?page_number=1&page_size=100&facet_filters=&sort=most_searched"

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 5)
driver.get(url)


try:
    ver_mais_button = driver.find_element(By.XPATH, "(//span[text()='Ver mais'])[2]")
    driver.execute_script("arguments[0].click();", ver_mais_button)

    secoes_cor = driver.find_elements(
        By.XPATH, "//summary[contains(text(), 'Cor')]/following-sibling::div//label"
    )

    print(secoes_cor)

    for secao in secoes_cor:
        cor = secao.text
        print(f"Cor encontrada: {cor}")

    print("Botão 'Ver mais' foi clicado com sucesso.")
except Exception as e:
    print(f"Erro ao tentar clicar no botão: {e}")

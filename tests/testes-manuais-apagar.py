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

cores = []
marcas = []

try:
    driver.execute_script("window.scrollTo(0, 900)")
    # ver_mais_cores = driver.find_element(By.XPATH, "(//span[text()='Ver mais'])[2]")
    # ver_mais_marcas = driver.find_element(By.XPATH, "(//span[text()='Ver mais'])[1]")

    espera = WebDriverWait(driver, 10)
    ver_mais_cores = espera.until(
        EC.presence_of_element_located((By.XPATH, "(//span[text()='Ver mais'])[2]"))
    )
    ver_mais_marcas = espera.until(
        EC.presence_of_element_located((By.XPATH, "(//span[text()='Ver mais'])[1]"))
    )
    print(ver_mais_cores)
    driver.execute_script(
        "arguments[0].click(); arguments[1].click();", ver_mais_cores, ver_mais_marcas
    )

    secoes_cor = driver.find_elements(
        By.XPATH, "//summary[contains(text(), 'Cor')]/following-sibling::div//label"
    )

    print(secoes_cor)

    for secao in secoes_cor:
        cor = secao.text
        print(f"Cor encontrada: {cor}")
        cores.append(cor)

    secoes_marca = driver.find_elements(
        By.XPATH, "//summary[contains(text(), 'Marcas')]/following-sibling::div//label"
    )

    for secao in secoes_marca:
        marca = secao.text
        print(f"Marca encontrada: {marca}")
        marcas.append(marca)

    print("Botão 'Ver mais' foi clicado com sucesso.")
except Exception as e:
    print(f"Erro ao tentar clicar no botão: {e}")

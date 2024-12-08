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

b = ".//article[contains(@class, 'productCard')]"

cartoes = wait.until(EC.presence_of_all_elements_located((By.XPATH, b)))

for cartao in cartoes:
    # print(cartao)
    elemento = cartao.find_element(By.XPATH, ".//img[contains(@class, 'imageCard')]")

    elem = elemento.get_attribute("title")
    print(elem)

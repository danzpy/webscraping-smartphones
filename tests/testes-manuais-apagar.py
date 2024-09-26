from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--log-level=3")
# chrome_options.add_argument("--headless")

url = "https://www.kabum.com.br/celular-smartphone/smartphones?page_number=1&page_size=100&facet_filters=&sort=most_searched"

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 30)
driver.get(url)


expandir = ".filterExpand"

filtros = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, expandir)))


for filtro in filtros:
    print(filtro)
    print("")
    filtro.click()


# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# c = ".sc-650252cf-2.hWvIRX.filterContent"
# c2 = '.sc-650252cf-3.dNkUXq'
# c3 = '.filterOption'

# infos = wait.until(
#     EC.presence_of_all_elements_located(
#         (By.CSS_SELECTOR, c3)
#     )
# )

# for info in infos:
# print(info)
# print(info.text)
#     elemento = info.find_element(By.CSS_SELECTOR, ".sc-650252cf-3.dNkUXq")

#     print(elemento.text)

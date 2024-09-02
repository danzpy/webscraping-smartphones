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

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

infos = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".sc-d43e0d1-7.cLeHop.productCard")
    )
)

for info in infos:
    elemento = info.find_element(By.CSS_SELECTOR, ".sc-d43e0d1-10.iruypF.productLink")

    print(elemento.get_attribute("href"))

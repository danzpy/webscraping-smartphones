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

url = "https://www.kabum.com.br/celular-smartphone/smartphones?page_number=19&page_size=100&facet_filters=&sort=most_searched"

# driver = webdriver.Chrome(options=chrome_options)
# wait = WebDriverWait(driver, 30)
# driver.get(url)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# info = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.next.disabled")))

df = pd.read_csv("informacoes-smartphones.csv", sep="|", encoding="utf-8")

print(df)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument('--log-level=3')
#chrome_options.add_argument("--headless")

url = 'https://www.kabum.com.br/celular-smartphone/smartphones'

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 30)
driver.get(url)

info = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sc-a638aad9-7.FeKTN.productCard")))

for i in info:
    print(i.text)

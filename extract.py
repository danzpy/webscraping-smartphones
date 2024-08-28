from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.kabum.com.br/celular-smartphone/smartphones'

class CustomOptions:

    def __init__(self) -> None:
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--allow-insecure-localhost")
        self.chrome_options.add_argument('--log-level=3')
        #self.chrome_options.add_argument("--headless")

    def espera(self, driver):
        self.tempo = 10
        return WebDriverWait(driver, self.tempo)

class Navegador:

    def __init__(self, url: str, options: CustomOptions) -> None:
        self.driver = webdriver.Chrome(options=options.chrome_options)
        self.options = options
        self.url = url

    def acessar_url(self) -> None:
        self.driver.get(self.url)

    def coletar_informacoes(self) -> None:
        espera = self.options.espera(self.driver)
        self.acessar_url()
        info = espera.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sc-a638aad9-7.FeKTN.productCard")))

        return info
        #return [elemento.text for elemento in info]

options = CustomOptions()
chrome = Navegador(url, options)

info = chrome.coletar_informacoes()

for i in info:
    img_element = i.find_element(By.CSS_SELECTOR, "img[title]")
    print(img_element.get_attribute('title'))
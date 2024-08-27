import requests.status_codes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

url = 'https://www.kabum.com.br/celular-smartphone/smartphones'

class CustomOptions:

    def __init__(self) -> None:
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--allow-insecure-localhost")
        self.chrome_options.add_argument('--log-level=3')
        self.chrome_options.add_argument("--headless")

    def espera(self, driver):
        self.tempo = 10
        self.aguardar = WebDriverWait(driver, self.tempo)


class Navegador:

    def __init__(self, url: str, options: CustomOptions) -> None:
        self.driver = webdriver.Chrome(options=options.chrome_options)
        self.url = url

    def validar_url(self) -> int:
        self.response = requests.get(self.url)
        self.status_code = self.response.status_code

        return self.status_code

    def acessar_url(self) -> None:
        options.espera(self.driver)
        self.driver.get(self.url)

options = CustomOptions()
chrome = Navegador(url, options)

if chrome.validar_url() == 200:
    print('foi')
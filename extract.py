from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


class CustomOptions:

    def __init__(self) -> None:
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--disable-3d-apis")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--allow-insecure-localhost")
        self.chrome_options.add_argument("--log-level=3")
        self.chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
        )
        self.chrome_options.add_argument("--headless")

    def espera(self, driver):
        self.tempo = 30
        return WebDriverWait(driver, self.tempo)


class Navegador:

    def __init__(self, options: CustomOptions) -> None:
        self.driver = webdriver.Chrome(options=options.chrome_options)
        self.options = options
        self.pagina = 1
        self.itens_por_pagina = 100
        self.base_url = "https://www.kabum.com.br/celular-smartphone/smartphones"
        self.dados_coletados = {"titulo": [], "preco": [], "link": []}

    def acessar_url(self, url=None) -> None:
        if url is None:
            url = f"{self.base_url}?page_number={self.pagina}&page_size={self.itens_por_pagina}&facet_filters=&sort=most_searched"
        self.driver.get(url)

    def coletar_informacoes(self, cartao) -> None:

        seletores = {
            "titulo": "img[title]",
            "preco": ".sc-b1f5eb03-2.iaiQNF.priceCard",
            "link": ".sc-a638aad9-10.hLaXrL.productLink",
        }

        acessar_pelo = {"titulo": "title", "preco": "text", "link": "href"}

        for chave, valor in seletores.items():
            elemento = cartao.find_element(By.CSS_SELECTOR, valor)

            if chave != "preco":
                self.dados_coletados[chave].append(
                    elemento.get_attribute(acessar_pelo[chave])
                )
            else:
                self.dados_coletados[chave].append(elemento.text)

    def coletar_cartoes(self) -> None:
        espera = self.options.espera(self.driver)
        cartoes = espera.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".sc-a638aad9-7.FeKTN.productCard")
            )
        )

        for cartao in cartoes:
            self.coletar_informacoes(cartao)

    def valida_ultima_pagina(self) -> bool:
        espera = self.options.espera(self.driver)
        try:
            ultima_pagina = espera.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "li.next.disabled"))
            )

            if ultima_pagina:
                print(
                    f"Cheguei na última página: {self.pagina}.\nDados extraídos com sucesso."
                )
                return True
        except:
            pass

    def proxima_pagina(self) -> None:
        self.pagina += 1
        proxima_pagina = f"{self.base_url}?page_number={self.pagina}&page_size={self.itens_por_pagina}&facet_filters=&sort=most_searched"
        self.acessar_url(proxima_pagina)

    def scraping(self) -> pd.DataFrame:
        self.acessar_url()
        while True:
            self.coletar_cartoes()
            if self.valida_ultima_pagina():
                break
            else:
                self.proxima_pagina()

        return pd.DataFrame(self.dados_coletados)


options = CustomOptions()
chrome = Navegador(options)

dados = chrome.scraping()
dados.to_csv(
    "/data/informacoes-smartphones.csv",
    sep="|",
    encoding="utf-8",
    header=True,
    index=False,
)

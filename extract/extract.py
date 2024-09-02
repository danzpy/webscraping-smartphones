from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os


class CustomOptions:
    """
    Classe responsável por aplicar as configurações do navegador Chrome para o WebDriver.

    Atributos:
    ----------
    chrome_options : Options
        Instância de opções do Chrome configurada com diversos argumentos.
    """

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
        # self.chrome_options.add_argument("--headless")

    def espera(self, driver) -> WebDriverWait:
        """
        Configura o tempo máximo de espera para que elementos estejam presentes na url especificada antes de interagir com eles.

        Parâmetros:
        -----------
        driver : WebDriver
            Instância do WebDriver que será usada para configurar a espera.

        Retorna:
        --------
        WebDriverWait
            Instância configurada de WebDriverWait.
        """
        self.tempo = 60
        return WebDriverWait(driver, self.tempo)


class Navegador:
    """
    Classe responsável por gerenciar o navegador e realizar o processo de scraping.

    -> Depende da classe "CustomOptions".

    Atributos:
    ----------
    driver : WebDriver
        Instância do WebDriver configurada com opções personalizadas.
    options : CustomOptions
        Instância da classe CustomOptions contendo as opções de configuração do navegador.
    pagina : int
        Número da página atual que está sendo processada.
    itens_por_pagina : int
        Número de itens exibidos por página no site.
    base_url : str
        URL base do site a ser raspado.
    dados_coletados : dict
        Dicionário que armazena os dados coletados como título, preço e link dos produtos.
    """

    def __init__(self, options: CustomOptions) -> None:
        self.driver = webdriver.Chrome(options=options.chrome_options)
        self.options = options
        self.pagina = 1
        self.itens_por_pagina = 100
        self.base_url = "https://www.kabum.com.br/celular-smartphone/smartphones"
        self.dados_coletados = {"titulo": [], "preco": [], "link": []}

    def acessar_url(self, url=None) -> None:
        """
        Acessa a URL especificada. Se nenhuma URL for passada, acessa a URL padrão configurada com base na página atual.

        Parâmetros:
        -----------
        url : str, opcional
            URL que será acessada. Se não especificada, será gerada a URL padrão baseada na página atual.

        Retorna:
        --------
        None
        """
        if url is None:
            url = f"{self.base_url}?page_number={self.pagina}&page_size={self.itens_por_pagina}&facet_filters=&sort=most_searched"
        self.driver.get(url)

    def coletar_informacoes(self, cartao) -> None:
        """
        Coleta informações do título, preço e link de um produto a partir de um cartão de produto na página.

        Parâmetros:
        -----------
        cartao : WebElement
            Elemento do cartão de produto de onde as informações serão extraídas.

        Retorna:
        --------
        None
        """

        seletores = {
            "titulo": "img[title]",
            "preco": ".sc-b1f5eb03-2.iaiQNF.priceCard",
            "link": ".sc-d43e0d1-10.iruypF.productLink",
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
        """
        Coleta todos os cartões de produtos presentes na página e extrai suas informações.

        Retorna:
        --------
        None
        """
        espera = self.options.espera(self.driver)
        cartoes = espera.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".sc-d43e0d1-7.cLeHop.productCard")
            )
        )

        for cartao in cartoes:
            self.coletar_informacoes(cartao)

    def valida_ultima_pagina(self) -> bool:
        """
        Verifica se a última página de resultados foi alcançada.

        Retorna:
        --------
        bool
            True se a última página foi alcançada, caso contrário False.
        """
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
        """
        Avança para a próxima página de resultados e acessa a URL correspondente.

        Retorna:
        --------
        None
        """
        self.pagina += 1
        proxima_pagina = f"{self.base_url}?page_number={self.pagina}&page_size={self.itens_por_pagina}&facet_filters=&sort=most_searched"
        self.acessar_url(proxima_pagina)

    def scraping(self) -> None:
        """
        Executa o processo completo de scraping, passando por todas as páginas disponíveis até a última.

        Retorna:
        --------
        None
        """
        self.acessar_url()
        while True:
            self.coletar_cartoes()
            print(f"Coleta da página {self.pagina} realizada com sucesso..")
            if self.valida_ultima_pagina():
                break
            else:
                self.proxima_pagina()

    def armazena_dados(self) -> None:
        """
        Armazena os dados coletados durante o processo de scraping em um arquivo CSV.

        Retorna:
        --------
        None
        """
        dados = pd.DataFrame(self.dados_coletados)

        data_directory = "data"
        file_path = os.path.join(data_directory, "informacoes-smartphones.csv")

        dados.to_csv(
            file_path,
            sep=";",
            encoding="utf-8",
            header=True,
            index=False,
        )

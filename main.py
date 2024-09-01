from extract.extract import CustomOptions, Navegador


options = CustomOptions()
chrome = Navegador(options)

# Realiza o processo de extração dos dados.
chrome.scraping()
chrome.armazena_dados()

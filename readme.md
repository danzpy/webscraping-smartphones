# Projeto de Web Scraping de Smartphones

Este projeto utiliza Selenium para fazer web scraping de informações sobre smartphones no site Kabum. O script Python coleta informações como modelo do smartphone, descrição, RAM, câmera e tela.

### Até o momento este projeto realiza as seguintes tarefas:

1. Utiliza o Selenium para abrir o Firefox e acessar a URL especificada.
2. Inclui rotinas de testes com pytest, taskipy
3. Encontra todos os elementos da página que correspondem à classe CSS dos cartões de produto.

### To do:

* Para cada produto, extrair as informações relevantes (modelo, descrição, RAM, câmera e tela) e as armazena em um dicionário.
* Utilizar expressões regulares para extrair informações específicas do texto da descrição.
* Adicionar o dicionário de informações do produto a um DataFrame do pandas.
* Incluir coluna de cor do smartphone (se houver na descrição do produto).
* Incluir coluna do processador do smartphone (se houver na descrição do produto).
* Coletar dados das demais páginas.
* Incluir rotina de pré commit, incluindo bibliotecas como black, blue, isort, etc.
* Incluir captura de logs através do sentry, loguru
* Modularizar a extração, transformação e carregamento
* Carregar em um banco de dados
* Utilizar docker neste projeto para que seja possível processa-lo em qualquer computador.
* Atualizar README.md, incluindo todo o passo a passo de como reproduzir o projeto.
* Criar uma imagem que descreva o workflow do projeto.

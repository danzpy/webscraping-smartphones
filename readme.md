# Projeto de Web Scraping de Smartphones

Este projeto utiliza Selenium para fazer web scraping de informações sobre smartphones no site Kabum. O script Python coleta informações como modelo do smartphone, descrição, RAM, câmera e tela.

O código funciona da seguinte maneira:

1. Utiliza o Selenium para abrir o Firefox e acessar a URL especificada.
2. Encontra todos os elementos da página que correspondem à classe CSS dos cartões de produto.
3. Para cada produto, extrai as informações relevantes (modelo, descrição, RAM, câmera e tela) e as armazena em um dicionário.
4. Utiliza expressões regulares para extrair informações específicas do texto da descrição.
5. Adiciona o dicionário de informações do produto a um DataFrame do pandas.

### To do:

* Incluir coluna de cor do smartphone (se houver na descrição do produto).
* Incluir coluna do processador do smartphone (se houver na descrição do produto).
* Corrigir coluna “smartphone model” quando não se pode utilizar o split(‘,’).
* Coletar dados das demais páginas.
* Incluir rotina de pré commit, incluindo bibliotecas como black, blue, isort, etc.
* Modularizar a extração, transformação e carregamento
* Carregar em um banco de dados
* Utilizar docker neste projeto para que seja possível processa-lo em qualquer computador.
* Atualizar README.md, incluindo todo o passo a passo de como reproduzir o projeto.
* Criar uma imagem que descreva o workflow do projeto.
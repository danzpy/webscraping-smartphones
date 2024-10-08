# Projeto de Web Scraping de Smartphones

Este projeto utiliza Selenium para fazer web scraping de informações sobre smartphones no site Kabum. O script Python coleta informações como modelo do smartphone, descrição, RAM, câmera e tela.

### Até o momento este projeto realiza as seguintes tarefas:

1. Utiliza o Selenium para abrir o Firefox e acessar a URL especificada.
2. Encontra todos os elementos da página que correspondem à classe CSS dos cartões de produto e extrai os dados.
3. Realiza a extração das demais páginas existentes na URL especificada.
4. Inclui rotinas de testes com pytest, taskipy
5. Inclui rotina de pré commit, utilizando black e outros hooks.
6. Armazena dados brutos em um CSV.

### To do:

* Para cada produto, extrair as informações relevantes (modelo, descrição, RAM, câmera, tela) utilizando expreções regulares. (Utilizar informações presentes nos filtros e localiza-las na descrição.)
* Incluir coluna de cor do smartphone (se houver na descrição do produto).
* Incluir coluna do processador do smartphone (se houver na descrição do produto).
* Incluir captura de logs através do sentry, loguru
* Modularizar a extração, transformação e carregamento
* Utilizar docker neste projeto para que seja possível processa-lo em qualquer computador.
* Carregar informações já tratadas em um banco de dados
* Atualizar README.md, incluindo todo o passo a passo de como reproduzir o projeto.
* Criar uma imagem que descreva o workflow do projeto.
* Fazer uma documentação do projeto utilizando Mkdocs.
* Identificar alguma forma de reduzir o tempo de extração (Tentar debugar adicionando logs de informação, na qual printe em qual etapa está procurando. Assim será evidente identificar o gargalo.)
* Tentar alterar a forma em que os elementos são procurados. Se caso não encontre algum, pule pro próximo (para dar tempo do que está ausente aparecer).
* Durante a execução do projeto, a estrutura do site mudou e algumas classes foram alteradas. Deixar isso evidente em algum lugar.
* Tentar adicionar alguma forma de extrair automaticamente as classes que se atualizam, com um XPATH que contenha alguma palavra em específica (ex: productCard), coisas que facilitem a extração sem precisar atualizar o código.

# python-speedio-challenge

## Teste de back-end

A aplicação consiste em uma API em Python + FastAPI e mongoDB como banco de dados.
A API realiza scraping de dados do website SimilarWeb, recebendo uma url e retornando os dados adquiridos.

Atualmente a aplicação utiliza um headless browser via selenium e chrome webdriver. Pretendo refazer a parte de scraping em breve sem automatizadores de navegação como selenium.

Acabei fazendo desse modo por praticidade, sabendo que funcionaria para burlar checagens de autenticação via javascript existentes no SimilarWeb, poupando tempo de desenvolvimento.

Obs.: A API faz uso de docker-compose apenas para simplificar a criação do banco de dados.

Para criar o banco de dados em um container docker, vá ate a raíz do projeto e digite <code>docker-compose up -d --build</code>

### Endpoints ->

<code>POST /salve_info</code> -> Recebe uma URL, realiza o scraping dos dados do SimilarWeb e os salva em um banco MongoDB.

<code>POST /get_info</code> -> Recebe uma URL, busca as informações no banco de dados e retorna para o usuário. Caso as informações ainda não estejam disponíveis, retorna um código de erro.

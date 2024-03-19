# python-speedio-challenge

## Teste de back-end

A aplicação consiste em uma API em Python + Flask e mongoDB como banco de dados.
A API realiza scraping de dados do website SimilarWeb, recebendo uma url e retornando os dados adquiridos.

### Endpoints ->

<code>POST /salve_info</code> -> Recebe uma URL, realiza o scraping dos dados do SimilarWeb e os salva em um banco MongoDB.

<code>POST /get_info</code> -> Recebe uma URL, busca as informações no banco de dados e retorna para o usuário. Caso as informações ainda não estejam disponíveis, retorna um código de erro.
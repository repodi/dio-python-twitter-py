# dio-twitter-py

Projeto criado durante o living code [Consumindo a API do Twitter com Python](https://docs.google.com/presentation/d/11DkkyQUIloVQLm8i6hN6w3xyUaP4WSRE/edit?usp=sharing&ouid=102662434190974209165&rtpof=true&sd=true).

## Tecnologias 📚

- Python 3.8.x
- FastAPI
- MongoDB

## Requisitos ✋

- Docker
- Docker compose

## Instalação 💽

Instale o [Docker](https://www.docker.com).

Instale o [Docker compose](https://docs.docker.com/compose/).
**Observação:** Nas ultimas versões do docker desktop o docker composer já vem instalado. 

Para executar e criar a máquina com o composer na pasta do projeto executar o comando no terminal:
```sh
docker-compose up -d
```
Para verificar se o ambiente foi instalado corretamente, executar o comando: 
```sh
docker-compose ps
```

## Configurações
### Configurações protegidas
Para criar as configurações protegidas como a a chave de API.

Criar um arquivo com o nome de *.env* na pasta raiz do projeto.

Dentro do arquivo informar as credencias de acesso a conta do twitter:
```
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
```
**Observação: como este arquivo contém informações que devem permanecer privadas, ele nunca deve ser subido para o repositório ou a chave da api estaria exposta.**

### Configurações gerais da aplicação

As configurações gerais da aplicação estão dentro do arquivo *app.conf*. 

Este arquivo não deve conter nenhuma informação sensível ou protegida, apenas configurações gerais. 


## Rodando a aplicação 🛸



Para iniciar a aplicação executar os comandos: 


```sh
poetry shell
python run main.py
```

Acesso o [Swagger UI](http://localhost:8000/docs) para listar todos os endpoints.

Use `Ctrl+C` para finalizar o processo servidor.

## Rodando os testes 🧪

```sh
poetry shell
poertry run pytest
```

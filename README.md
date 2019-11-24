# Eventex

Sistema de Eventos encomendado pela Morena

[![Build Status](https://travis-ci.com/mbgarcia/eventex.svg?branch=master)](https://travis-ci.com/mbgarcia/eventex)

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv
3. Ative o virtualenv
4. Instale as depêndencias
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:mbgarcia/eventex.git wttd
cd wttd
python -m venv .wttd
  ou
  virtualenv wttd
. .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
  ou
  manage test (se tiver o alias criado) 
```

## Como fazer o deploy?

1. Crie uma instância no Heroku
2. Envie as configurações para o Heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o Heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib\secret_gen.py`
heroku config:set DEBUG=False
# configura o email
git push heroky master --force 
```
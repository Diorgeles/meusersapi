# Desafio GrupoAndradeMartins

API desenvolvido para o desafio do grupo andrade martins.

[Clique aqui e abra o projeto](https://meusersapi.herokuapp.com/) e para acessar o [admin](https://meusersapi.herokuapp.com/admin/login/?next=/admin/)

Insira os dados:

usuario: lucassrod@gmail.com
senha: apresentacao123

## Tecnologias utilizadas

* Django 1.10
* SQLite
* Django Rest Framework
* Django JWT
* DRF Token

## Considerações do desafio

Lista com as considerações acerca do desenvolvimento

### Token

Utilizado o pacote do [DRF](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)

```python
INSTALLED_APPS = (
    ...
    'rest_framework.authtoken'
)
```

Criado signal no `accounts.model`

```python
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

post_save.connect(create_auth_token, sender=CustomUser)
```

### JWT

De acordo com [DRF JsonWebToken](http://www.django-rest-framework.org/api-guide/authentication/#json-web-token-authentication) foi utilizado o pacote [DRF-JWT](https://github.com/GetBlimp/django-rest-framework-jwt)

Configurações

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    ....
}
```

### Modelo de usuarios

O modelo de usuario deste projeto foi customizado para incluir o campo code como sendo do tipo UUID


No arquivo de configuração `me/settings/base.py` temos:

```python
AUTH_USER_MODEL = 'accounts.CustomUser'
```

No modelo em `accounts/models.py` temos a classe `class CustomUser(...)` com o campo uuid além da primary key id.

```python
code = models.UUIDField(
    default=uuid.uuid4,
    editable=False,
    unique=True
)
```

### Cadastro de usuários

Endpoint: `POST http://meusersapi.herokuapp.com/users/`

> Não consegui passar uma lista e um dicionario para este endpoint. Portanto o cadastro acabou sendo feito manual, não utilizando os serializers

```json
{
    "name": "José Soares",
    "email": "jose@soares.com",
    "password": "secret",
    "address": [
        {
            "street": "rua abc",
            "number": "210",
            "distric": "centro",
            "city": "Belo Horizonte",
            "state": "MG",
            "country": "Brasil"
        }
    ]
}
```

### Login

Não realizei a implementação manual do login pois o framework me fornece praticamente todos os tipos de autenticação, bastando passar no cabeçalho as informações corretas de `Authorization: Token` ou `Authorization: JWT`


### Perfil do Usuário

Endpoint `GET http://meusersapi.herokuapp.com/users/me/profile/ "Authorization: Token 37155bfb98e11983d23d7ffd5ed0a51930bd053c"`

Retorna o perfil do usuario que esta chamando a rota

Outros usuários cadastrados

Endpoint `GET http://meusersapi.herokuapp.com/users/`
Endpoint `GET http://meusersapi.herokuapp.com/users/paginated/\?page\=2`


Outros perfis:

Endpoint `GET http://meusersapi.herokuapp.com/users/profile/f06a2a3e-4387-46c3-9626-c31d2a696725/`


## Como instalar

Clone o projeto


```shell

$ git clone git@github.com:lucassimon/meusersapi.git
$ cd meusersapi

```

Crie um virtualenv em sua maquina.


```shell

$ mkvirtualenv -p /usr/bin/python3 usersapi

```

Instale os pacotes necessários


```shell

$ pip install -r requirements/dev.txt

```

Execute as migrations


```shell

$ python manage.py migrate --settings=me.settings.dev

```

Crie um superusuario

```shell

$ python manage.py createsuperuser --settings=me.settings.dev

```

Crie um perfil para este super usuario

```

python manage.py shell_plus --settings=me.settings.dev

In [1]: user = CustomUser.objects.latest('id')

In [2]: Profile.objects.create(user=user, name='Lucas Simon')
Out[2]: <Profile: lucassrod@gmail.com>

```


## Executar o projeto

Execute no terminal

```shell

python manage.py runserver --settings=me.settings.dev

```

### Comandos a serem executados para acesso da API

Utilizado os comandos [http](https://httpie.org/) ou curl.


1. Autenticação por JWT

```shell
http -v -f POST http://meusersapi.herokuapp.com/api-token-auth/ email="lucassrod@gmail.com" password="apresentacao123"
```

```json
POST /api-token-auth/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 52
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: meusersapi.herokuapp.com
User-Agent: HTTPie/0.8.0

email=lucassrod%40gmail.com&password=apresentacao123

HTTP/1.1 200 OK
Allow: POST, OPTIONS
Connection: close
Content-Type: application/json
Date: Wed, 29 Mar 2017 23:51:19 GMT
Server: WSGIServer/0.2 CPython/3.6.0
Vary: Accept
Via: 1.1 vegur

{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6Imx1Y2Fzc3JvZEBnbWFpbC5jb20iLCJ1c2VybmFtZSI6Imx1Y2Fzc3JvZEBnbWFpbC5jb20iLCJleHAiOjE0OTA4MzE3Nzl9.FsH_ulajrlivse9sTcHrWez5Zy6xZfNoqa7pmQct5aw"
}

```

2. Acesso a rota atraves de JWT

```shell
$ http -v GET http://meusersapi.herokuapp.com/users/ "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6Imx1Y2Fzc3JvZEBnbWFpbC5jb20iLCJ1c2VybmFtZSI6Imx1Y2Fzc3JvZEBnbWFpbC5jb20iLCJleHAiOjE0OTA4MzE3Nzl9.FsH_ulajrlivse9sTcHrWez5Zy6xZfNoqa7pmQct5aw"
```

```json
GET /users/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization:  JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6Imx1Y2Fzc3JvZEBnbWFpbC5jb20iLCJ1c2VybmFtZSI6Imx1Y2Fzc3JvZEBnbWFpbC5jb20iLCJleHAiOjE0OTA4MzE3Nzl9.FsH_ulajrlivse9sTcHrWez5Zy6xZfNoqa7pmQct5aw
Connection: keep-alive
Host: meusersapi.herokuapp.com
User-Agent: HTTPie/0.8.0



HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Connection: close
Content-Type: application/json
Date: Wed, 29 Mar 2017 23:52:38 GMT
Server: WSGIServer/0.2 CPython/3.6.0
Vary: Accept
Via: 1.1 vegur

[
    {
        "address": [],
        "code": "58f2c657-9810-4755-ac73-e650fa2d32a4",
        "created": "2017-03-29T23:34:56.363296Z",
        "email": "lucassrod@gmail.com",
        "last_login": "2017-03-29T23:35:21.335680Z",
        "modified": "2017-03-29T23:34:56.376491Z",
        "name": "Lucas Simon",
        "profile": {
            "code": "f36adf94-ab41-4182-b02d-d9f0083d29f6",
            "id": 1,
            "name": "Lucas Simon"
        },
        "token": "37155bfb98e11983d23d7ffd5ed0a51930bd053c"
    }
]
```

3. Acesso via Token

```shell
http -v GET http://meusersapi.herokuapp.com/users/ "Authorization: Token 37155bfb98e11983d23d7ffd5ed0a51930bd053c"
```

```json
GET /users/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization:  Token 37155bfb98e11983d23d7ffd5ed0a51930bd053c
Connection: keep-alive
Host: meusersapi.herokuapp.com
User-Agent: HTTPie/0.8.0



HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Connection: close
Content-Type: application/json
Date: Wed, 29 Mar 2017 23:53:41 GMT
Server: WSGIServer/0.2 CPython/3.6.0
Vary: Accept
Via: 1.1 vegur

[
    {
        "address": [],
        "code": "58f2c657-9810-4755-ac73-e650fa2d32a4",
        "created": "2017-03-29T23:34:56.363296Z",
        "email": "lucassrod@gmail.com",
        "last_login": "2017-03-29T23:35:21.335680Z",
        "modified": "2017-03-29T23:34:56.376491Z",
        "name": "Lucas Simon",
        "profile": {
            "code": "f36adf94-ab41-4182-b02d-d9f0083d29f6",
            "id": 1,
            "name": "Lucas Simon"
        },
        "token": "37155bfb98e11983d23d7ffd5ed0a51930bd053c"
    }
]

```

4. Cadastro de usuário via curl

```shell
curl -v -X POST http://meusersapi.herokuapp.com/users/ -H "Authorization: Token 37155bfb98e11983d23d7ffd5ed0a51930bd053c" -d email="teste2@teste.com" -d name="teste"  -d password='123' -d city='Belo Horizonte' -d country='Brasil' -d district='Centro' -d number='1137' -d state='Minas Gerais' -d street='avenida amazonas'
```

```json
* Closing connection 0
{"code":"32bb29ca-00a2-4212-9fc7-bb0d9e6522ce","email":"teste1@teste.com","profile":{"id":2,"name":"teste","code":"c0c4727b-4ade-471c-bd81-d5e8dfcca577"},"name":"teste","address":[{"id":1,"street":"avenida amazonas","number":"1137","district":"Centro","city":"Belo Horizonte","state":"Minas Gerais","country":"Brasil"}],"token":"91bae49227595e54bc59c2896d6463efa9dff08c","created":"2017-03-29T23:55:16.809916Z","modified":"2017-03-29T23:55:16.809980Z","last_login":null}
```

5. Cadastro de usuário via http

Com erro de email ja existente


```shell
http -v -f POST http://meusersapi.herokuapp.com/users/ "Authorization: Token 37155bfb98e11983d23d7ffd5ed0a51930bd053c" email="teste1@teste.com" name="teste" password='123' city='Belo Horizonte' country='Brasil' district='Centro' number='1137' state='Minas Gerais' street='avenida amazonas'
```

```json
POST /users/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization:  Token 37155bfb98e11983d23d7ffd5ed0a51930bd053c
Connection: keep-alive
Content-Length: 154
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: meusersapi.herokuapp.com
User-Agent: HTTPie/0.8.0

email=teste1%40teste.com&name=teste&password=123&city=Belo+Horizonte&country=Brasil&district=Centro&number=1137&state=Minas+Gerais&street=avenida+amazonas

HTTP/1.1 400 Bad Request
Allow: GET, POST, HEAD, OPTIONS
Connection: close
Content-Type: application/json
Date: Wed, 29 Mar 2017 23:57:50 GMT
Server: WSGIServer/0.2 CPython/3.6.0
Vary: Accept
Via: 1.1 vegur

{
    "errors": {
        "email": [
            "Usuário com este endereço de email já existe."
        ]
    }
}
```

Com sucesso de email ja existente

```shell
http -v -f POST http://meusersapi.herokuapp.com/users/ "Authorization: Token 37155bfb98e11983d23d7ffd5ed0a51930bd053c" email="teste2@teste.com" name="teste" password='123' city='Belo Horizonte' country='Brasil' district='Centro' number='1137' state='Minas Gerais' street='avenida amazonas'
```

```json
POST /users/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization:  Token 37155bfb98e11983d23d7ffd5ed0a51930bd053c
Connection: keep-alive
Content-Length: 154
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: meusersapi.herokuapp.com
User-Agent: HTTPie/0.8.0

email=teste2%40teste.com&name=teste&password=123&city=Belo+Horizonte&country=Brasil&district=Centro&number=1137&state=Minas+Gerais&street=avenida+amazonas

HTTP/1.1 201 Created
Allow: GET, POST, HEAD, OPTIONS
Connection: close
Content-Type: application/json
Date: Wed, 29 Mar 2017 23:58:54 GMT
Server: WSGIServer/0.2 CPython/3.6.0
Vary: Accept
Via: 1.1 vegur

{
    "address": [
        {
            "city": "Belo Horizonte",
            "country": "Brasil",
            "district": "Centro",
            "id": 2,
            "number": "1137",
            "state": "Minas Gerais",
            "street": "avenida amazonas"
        }
    ],
    "code": "ac8c1a6c-d07c-410e-83ac-8b7f19ba49e2",
    "created": "2017-03-29T23:58:54.815629Z",
    "email": "teste2@teste.com",
    "last_login": null,
    "modified": "2017-03-29T23:58:54.815663Z",
    "name": "teste",
    "profile": {
        "code": "f06a2a3e-4387-46c3-9626-c31d2a696725",
        "id": 3,
        "name": "teste"
    },
    "token": "3007ae0e1cb9117a06796d1cea4a28e1d47120af"
}
```
# {{ cookiecutter.project_name }}

Esse é um projeto Scrapy adequado para rodar na plataforma [Scrapinghub](https://scrapinghub.com/).

### Features

* Python 3.5
* Scrapy 1.5

# Executando localmente

Existem três formas de executar o projeto de forma local:

* Usando um container Docker
* Executando o spider usando o utilitário **scrapy**
* Executando o script utilitário **run_spiders.py**

## Executando com docker container

### BUILDING the docker container

```sh
$ make build
```

### RUNNING

Para executar todos os spiders dentro do projeto use:
```sh
$ make run
```
Para executar um spider específico use:
```sh
$ make run SPIDER='spider_1 spider_2'
```
## Executando com script run_spiders.py

Para executar todos os spiders dentro do projeto use:
```sh
$ python3 scripts/run_spiders.py
```

Para executar um spider específico use:
```sh
$ python3 scripts/run_spiders.py --s spider_1 spider_2
```

## Executando com scrapy

```sh
$ scrapy crawl <nome do spider> -o output/out.csv
```

# Realizando deploy no [Scrapinghub](https://scrapinghub.com/).

Para realizar o deploy na plataforma é necessário realizar o login através utilitário '[shub](https://pypi.org/project/shub/)' com o comando:

```sh
$ shub login
```

Feito o login o deploy é feito com o comando:

```sh
$ make release
```

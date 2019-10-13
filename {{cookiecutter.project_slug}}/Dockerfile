FROM scrapinghub/scrapinghub-stack-scrapy:1.6-py3

WORKDIR /app
ADD requirements.txt /app

RUN set -x \
    && pip --no-cache-dir \
      --disable-pip-version-check \
      install -r /app/requirements.txt

ADD . /app

CMD ["scrapy", "list"]
# CMD ["scrapy", "crawl", "{{cookiecutter.project_slug}}", "-o", "output/out.csv"]

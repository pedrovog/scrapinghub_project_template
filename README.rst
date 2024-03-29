Cookiecutter Scrapy Project Template
====================================

A bare minimum cookiecutter template for a Scrapy project.

What is included:

* Default stack is Scrapy 1.5 and Python 3.5.
* Standard project files generated by ``scrapy startproject``.
* A default ``requirements.txt``.
* A default ``scrapinghub.yml``, `Scrapy Cloud`_ configuration file.
* A default ``Dockerfile`` to build a docker image to replicate the
  `Scrapy Cloud`_ running container.

Usage
-----

1. Install ``cookiecutter`` if you do not have it already: ``pip install cookiecutter``

2. Generate a new project: ``cookiecutter https://github.com/pedrovog/scrapinghub_project_template``

Example
-------
We will show how to create and deploy a `Scrapy`_ project to `Scrapy Cloud`_. You
will need to have an account in `Scrapy Cloud`_ and a Scrapy Project already
created. In this example, we use OSX as development machine.

First we bootstrap our project and create a spider:

.. code-block::

  $ cookiecutter https://github.com/pedrovog/scrapinghub_project_template
  project_name [Project Name]: myproject
  project_slug [myproject]:
  project_module [myproject]:
  scrapycloud_id [Scrapy Cloud Project ID]: 12345
  $ cd myproject
  $ pip install -r requirements.txt -r dev-requirements.txt
  $ cat > myproject/spiders/myspider.py <<EOF
  import scrapy

  class BlogSpider(scrapy.Spider):
      name = 'blogspider'
      start_urls = ['https://blog.scrapinghub.com']

      def parse(self, response):
          for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
              yield scrapy.Request(response.urljoin(url), self.parse_titles)

      def parse_titles(self, response):
          for post_title in response.css('div.entries > ul > li a::text').extract():
              yield {'title': post_title}

  EOF

Now we can run the spider in our host::

  $ scrapy crawl blogspider

Also we can build a docker image to replicate the `Scrapy Cloud`_ container::

  $ docker build -t myproject .
  $ docker run -it myproject scrapy crawl blogspider

Finally, we can deploy to our `Scrapy Cloud`_ project and schedule the spider::

  $ shub deploy
  $ shub schedule blogspider
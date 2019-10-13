# -*- coding: utf-8 -*-

import scrapy
from scrapy import spiderloader
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

import argparse
from twisted.internet import reactor

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--s', '-scraper',
        metavar='scraper',
        type=str,
        default=[],
        nargs='+',
        help="""Scrapers para rodar"""
    )

    args = parser.parse_args()

    if args.s:
        spiders = args.s
    else:
        spiders = spiderloader.SpiderLoader.from_settings(get_project_settings()).list()

    runner = CrawlerRunner(get_project_settings())

    spider_loader = spiderloader.SpiderLoader(get_project_settings())
    process = CrawlerProcess(get_project_settings())
    for spider in spiders:
        spider = spider_loader.load(spider_name=spider)
        runner.crawl(spider)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()

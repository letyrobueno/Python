"""
  Spider to scrape the list of laptops on the Walmart Canada website to help us compare them
  and make a good decision about which one to buy.
  It uses Scrapy, Splash, and the library scrapy-splash.
"""
import scrapy

# Easiest way to render requests with Splash
from scrapy_splash import SplashRequest
import pandas as pd
import time

class WalmartLaptopsSpider(scrapy.Spider):
  name = 'walmart_laptops'
  allowed_domains = ['www.walmart.ca']
  start_urls = ['https://www.walmart.ca/en/electronics/laptops-computers/laptops-notebooks/N-1855/']

  def start_requests(self):
    for url in self.start_urls:
      yield SplashRequest(url=url, callback=self.parse, endpoint='render.html')

  def parse(self, response):
    for laptop in response.css('a.product-link'):
      item = {
              'URL': laptop.css('::attr(href)').extract_first(),
              'Name': laptop.css('h2.thumb-header::text').extract_first(),
              'Description': laptop.css('div.description::text').extract_first()
             }
      items.append(item)

    now = time.strftime("%Y-%m-%d-%Hh%M")

    df = pd.DataFrame(items, columns=['URL', 'Name', 'Description'])
    df.to_csv('laptops_walmart_' + now + '.csv', sep=',')

items = []
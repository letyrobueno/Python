"""
  Spider to scrape the list of laptops on the Best Buy Canada website to help us compare them
  and make a good decision about which one to buy.
  It takes only the laptops at https://www.bestbuy.ca/en-ca/category/laptops/36711
  It does not go through the other pages.
"""


import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess
from datetime import datetime

class laptop_spider(scrapy.Spider):
   """ Takes info from the list of laptops at bestbuy.ca.
   """

   # Name is not necessarily the class' name, just must be unique
   # Intend to help us track the spider
   name = 'laptop_spider' # mandatory line

   # Domains allowed to get crawled
   allowed_domains = ['bestbuy.ca']
   start_urls = ['https://www.bestbuy.ca/en-ca/category/laptops/36711']

   # Callback function called whenever a URL in start_urls is crawled successfully
   def parse(self, response):
      """ Function to take the urls of the laptops so we can get the info we want
          to compare the laptops
      """
      laptops_links = response.css('div.x-productListItem > div > a::attr(href)').extract()
      for url in laptops_links:
         yield response.follow(url = url, callback = self.parse_pages)

   def parse_pages(self, response):
      """ Function to parse each product's page to take some information
          about the product.
      """
      # Name of a property (memory, processor, etc) of the laptop
      props_titles = response.css('div.itemName_jGrp0::text').extract()
      # Value of the property of the laptop
      props = response.css('div.itemValue_341-l::text').extract()
      item = {
              'Name': response.css('h1.productName_19xJx::text').extract_first(),
              'Price': response.css('div.price_FHDfG::text').extract_first(), 
              'Model': response.css('div.modelInformation_1WYvb > span[itemprop=model]::text').extract_first(),
              'Proc Type': props[props_titles.index('Processor Type')],
              'Proc Cores': props[props_titles.index('Processor Cores')],
              'Proc Speed': props[props_titles.index('Processor Speed')],
              'RAM': props[props_titles.index('RAM Size')],
              'OS': props[props_titles.index('Pre-loaded Operating System')],
              'url': response.request.url
             }
      items.append(item)

items = []

process = CrawlerProcess()
process.crawl(laptop_spider)
process.start()

now = str(datetime.now())

df = pd.DataFrame(items, columns=['Name', 'Price', 'Model', 'Proc Type', 'Proc Cores', 'Proc Speed', 'RAM', 'OS', 'url'])
df.to_csv('laptops_bestbuy_' + now + '.csv', sep=',')

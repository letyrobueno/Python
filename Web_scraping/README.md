# Web Scraping

[Scrapy Tutorial](https://www.datacamp.com/community/tutorials/making-web-crawlers-scrapy-python):

Scrapy provides a web-crawling shell so we can use to see what components the Web page returns and how you can use them.

### Using Scrapy Shell in a Python environment:
`(env) $ scrapy shell`
`      : fetch('https://www.aliexpress.com/category/200216607/tablets.html')`
`      : view(response)              // Web page will be opened in the default browser`
`      : print(response.text)        // Shows the script that generates the Web page`
`      : response.css(".product::text").extract_first()  // CSS Selector example`
`      : response.xpath('/html').extract()               // xpath selector example`
`      : response.css('html').extract()`
`      : scrapy startproject test                        // Creates a hidden folder for your project`
`      : exit                                            // to leave the Scrapy shell`

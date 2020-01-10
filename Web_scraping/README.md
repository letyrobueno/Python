# Web Scraping

[Scrapy Tutorial](https://www.datacamp.com/community/tutorials/making-web-crawlers-scrapy-python):

Scrapy provides a web-crawling shell so we can use to see what components the Web page returns and how you can use them.

### Using Scrapy Shell in a Python environment:
```
(env) $ scrapy shell
(env) $ fetch('https://www.aliexpress.com/category/200216607/tablets.html')
(env) $ view(response)                                  // Web page will be opened in default browser
(env) $ print(response.text)                            // Shows script that generates the Web page
(env) $ response.css(".product::text").extract_first()  // CSS Selector example
(env) $ response.xpath('/html').extract()               // xpath selector example
(env) $ response.css('html').extract()
(env) $ scrapy startproject test                        // Creates a hidden folder for your project
(env) $ exit                                            // to leave the Scrapy shell```

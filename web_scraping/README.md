# Web Scraping

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
(env) $ exit                                            // to leave the Scrapy shell
```

### Scraping static and dynamic websites

#### Static websites (info in the HTML):

* [CSS selectors example](https://github.com/letyrobueno/Python/blob/master/web_scraping/css_selectors.py)
* [xpath selectors example](https://github.com/letyrobueno/Python/blob/master/web_scraping/xpath_selectors.py)
* [Chaining both CSS and xpath selectors](https://github.com/letyrobueno/Python/blob/master/web_scraping/chaining_xpath_css_selectors.py)
* [Scrapy example](https://github.com/letyrobueno/Python/blob/master/web_scraping/spider_bestbuy_scrapy.py)

#### Dynamic websites (info rendered by Javascript):
Tools like [Scrapy](https://scrapy.org/), [Sky](http://docs.python-requests.org/en/master/), [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Requests](http://docs.python-requests.org/en/master/) only retrieve static HTML, not the dynamic part rendered by Javascript. In these cases:
1. Intercept AJAX calls and reproduce them. [Example using Requests library](https://github.com/letyrobueno/Python/blob/master/web_scraping/spider_bestbuy_scrapy.py)

2. Use automated browsers like [Selenium](https://selenium.dev/) and [Splash](https://splash.readthedocs.io/en/stable/).


### Links:
* [Scrapy Tutorial and Documentation](https://docs.scrapy.org/en/latest/intro/tutorial.html)

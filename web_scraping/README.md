# Web Scraping

Scrapy provides a web-crawling shell so we can use to see what components the Web page returns and how you can use them.

### Using Scrapy Shell in a Python environment:
```
(env) $ scrapy shell
In [1]: fetch('https://www.aliexpress.com/category/200216607/tablets.html')
In [2]: view(response)                                  // Web page will be opened in default browser
In [3]: print(response.text)                            // Shows script that generates the Web page
In [4]: response.css(".product::text").extract_first()  // CSS Selector example
In [5]: response.xpath('/html').extract()               // xpath selector example
In [6]: response.css('html').extract()
In [7]: scrapy startproject test                        // Creates a Scrapy project
In [8]: scrapy genspider test https://www.google.com    // Creates a spider inside test/spiders directory
In [9]: scrapy crawl test 								// Run spider
In [10]: exit                                            // to leave the Scrapy shell
```

* To save data, add the following to the `settings.py` (it will append the data every time we run the spider):
```
FEED_FORMAT="csv"
FEED_URI="dataset_test.csv"
```

### Scraping static and dynamic websites

#### Static websites (info in the HTML):

* [CSS selectors example](https://github.com/letyrobueno/Python/blob/master/web_scraping/css_selectors.py)
* [xpath selectors example](https://github.com/letyrobueno/Python/blob/master/web_scraping/xpath_selectors.py)
* [Chaining both CSS and xpath selectors](https://github.com/letyrobueno/Python/blob/master/web_scraping/chaining_xpath_css_selectors.py)
* [Scrapy example](https://github.com/letyrobueno/Python/blob/master/web_scraping/spider_bestbuy_scrapy.py)

#### Dynamic websites (info rendered by Javascript):
Tools like [Scrapy](https://scrapy.org/), [Sky](http://docs.python-requests.org/en/master/), [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Requests](http://docs.python-requests.org/en/master/) only retrieve static HTML, not the dynamic part rendered by Javascript. In these cases:
1. Intercept AJAX calls and reproduce them.<br>
[Example using Requests library](https://github.com/letyrobueno/Python/blob/master/web_scraping/spider_bestbuy_requests.py)

2. Use automated browsers like [Selenium](https://selenium.dev/) (too resource-consuming) and [Splash](https://splash.readthedocs.io/en/stable/) (it renders JS content only).<br>
[Installing Splash](https://github.com/letyrobueno/Python/blob/master/web_scraping/splash.md)<br>
Example with Splash and Scrapy.

### Links:
* [Scrapy Tutorial and Documentation](https://docs.scrapy.org/en/latest/intro/tutorial.html)

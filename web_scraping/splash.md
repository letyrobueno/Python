# Installing [Splash](http://splash.readthedocs.io/)

1. Install [Docker](https://www.docker.com/):
```$ sudo apt install docker.io```

2. Install Splash:
```$ sudo docker pull scrapinghub/splash```

3. Start Splash server:
```$ sudo docker run -p 8050:8050 scrapinghub/splash```
Splash service will be on [http://localhost:8050](http://localhost:8050s)

# Creating a [Scrapy-Splash](https://github.com/scrapy-plugins/scrapy-splash) project

1. Install `scrapy-splash`:
```(env) $ python3 -m pip install scrapy-splash --user```

2. Create a scrapy project:
```(env) $ scrapy startproject walmart_spider```

# Integrating Scrapy and Splash
1. Add the Splash server address to `settings.py` inside the project folder:
```SPLASH_URL = 'http://localhost:8050'```
OR SOMETHING LIKE:
```SPLASH_URL = 'http://192.168.59.103:8050'```

2. Still in `settings.py`, set: 
```
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
```

# Constructing the spider

1. Create a Scrapy project:
```
scrapy startproject walmart_spider
```
2. Create a spider inside the project `walmart_spider/spiders`:
```
(env) $ scrapy genspider walmart_laptops https://www.walmart.ca/en/electronics/laptops-computers/laptops-notebooks/N-1855
```
3. Program the spider and, inside the project directory, run:
```
scrapy crawl walmart_laptops
```

### Links:
* [Splash Scripts Tutorial](https://splash.readthedocs.io/en/stable/scripting-tutorial.html)
* [Example in scrapy-splash GitHub page](https://github.com/scrapy-plugins/scrapy-splash/blob/master/example/scrashtest/spiders/quotes.py)

from scrapy import Selector

html = '''
<html>
   <body>
      <div class="hello" id="uid">
         <p>Testing scrapy library!</p>
         <p class="classy">Second paragraph!</p>
         <a href="http://www.google.com">Google</a>
         <a href="https://github.com/">GitHub</a>
      </div>
      <p id="par">Let us have fun!</p>
      <p class="class-1">La la land</p>
   </body>
</html>
'''

sel = Selector(text = html)

# Select all hyperlinks of div elements belonging to class "hello"
hyperlinks = sel.css('div.hello > a')

# Select all href attributes (chaining with a css selector)
hrefs_from_css = hyperlinks.css('::attr(href)').extract()
print('CSS:   ', hrefs_from_css)

# Select all href attributes (chaining with a xpath)
# **** DON'T FORGET: ***** use dot to concatenate
hrefs_from_xpath = hyperlinks.xpath('./@href').extract()
print('xpath: ', hrefs_from_xpath)
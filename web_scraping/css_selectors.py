from scrapy import Selector
import requests

# Taking content from a Web page
url = 'https://leticia.compscinet.org/'
html_web = requests.get(url).content


html = '''
<html>
   <body>
      <div class="hello" id="uid">
         <p>Testing scrapy library!</p>
         <p class="classy">Second paragraph!</p>
         <a href="http://www.google.com">Google</a>
      </div>
      <p id="par">Let us have fun!</p>
      <p class="class-1">La la land</p>
   </body>
</html>
'''
print(html)

sel = Selector(text = html)

# This returns a SelectorList of Selector objects
paragraphs = sel.css('div > p')

# ******* EXTRACT DATA FROM A SELECTORLIST *******
print('\nEXTRACT DATA FROM A SELECTORLIST')
# Gives all Selector objects inside the Selector list
results = sel.css('div > p').extract()
print('\n1. Gives all selector objects inside the selector list:')
print('RESULT:\t', results)

# Gives only the 1st element of the Selector list
first_result = sel.css('div > p').extract_first()
print('\n2. Gives only the 1st element of the Selector list:')
print('RESULT:\t', first_result)

# Choosing an object inside the Selector list
second_result = results[1]


# ******* EXAMPLES OF SELECTIONS *******
# Note that: * searches all in the same level; 
# while // searches all in all levels of depth.
print('\nEXAMPLES OF SELECTIONS')

# Select the hyperlink children of all div elements whose is "course-block"
hyperlink = sel.css("div.hello > a").extract()
print('\n1. Select the hyperlink children of all div elements whose class is "hello":')
print('RESULT:\t', hyperlink)

# Search any level of depth for paragraphs in div elements whose id = uid
uid_p = sel.css('div#uid > p:nth-of-type(2)').extract() # In xpath: '//div[@id="uid"]/p[2]'
print('\n2. Search any level of depth for paragraphs in div elements whose id = uid:')
print('RESULT:\t', uid_p)

# Search all levels of depth for div elements whose id = uid, 
# then for span and then for h4 in all levels
uid_span = sel.css('div#uid > span h4') # In xpath: '//div[@id="uid"]/span//h4'
print('\n3. Selection used: //div[@id="uid"]/span//h4:')
print('RESULT:\t', uid_span)

# Select paragraph elements within class 'class1'
class1_p = sel.css('div#uid > p.class-1')

# Select all elements whose class attribute belongs to class1
class1_all = sel.css('.class-1')

# All children of the element whose id is uid
all_children_uid = sel.css('#uid > *')

# Select all elements belonging to class-1
class1_all = sel.css('*.class-1') # Same as: sel.css('.class-1')

# Select element with id attribute equal to uid
uid = sel.css('*#uid') # Same as: sel.css('#uid')

# From div with id=uid select hyperlink
# Double colon: to select the attribute
sel.css('div#uid > a::attr(href)') # In xpath: '//div[@id="uid"]/a/@href'

# Text Extraction

# OR for all elements (add space): sel.css('p#par ::text').extract()
text_p = sel.css('p#par::text').extract() 
print('\nText Extraction:')
print('RESULT:\t', text_p)
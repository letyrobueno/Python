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
paragraphs = sel.xpath('//p')

# ******* EXTRACT DATA FROM A SELECTORLIST *******
print('\n******* EXTRACT DATA FROM A SELECTORLIST *******')

# Gives all Selector objects inside the Selector list
results = sel.xpath('//p').extract()
print('\n1. Gives all selector objects inside the selector list:')
print('\nRESULT:\t', results)

# Gives only the 1st element of the Selector list
first_result = sel.xpath('//p').extract_first()
print('\n2. Gives only the 1st element of the selector list:')
print('\nRESULT:\t', first_result)

# Choosing an object inside the Selector list
second_result = paragraphs[1]

# ******* EXAMPLES OF SELECTIONS *******
# Note that: * searches all in the same level; 
# while // searches all in all levels of depth.
print('\n******* EXAMPLES OF SELECTIONS *******')

# Give total number of children of the first paragraph element
total_children = len(paragraphs[0].xpath('./*'))


# Select all children of the first div element
divs = sel.xpath('//div')
total_children = divs[0].xpath('./*').extract()
print('\n1. Select all children of the first div element:')
print('RESULT:\t', total_children)

# Search in any level of depth or breadth for the element whose id is uid
uid = sel.xpath('//*[@id="uid"]').extract()
print('\n2. Search in any level of depth or breadth for the element whose id is uid:')
print('RESULT:\t', uid)

# Search in any level of depth for 2nd paragraph in div elements whose id = uid
uid_p = sel.xpath('//div[@id="uid"]/p[2]').extract()
print('\n3. Search in any level of depth for 2nd paragraph in div elements whose id = uid:')
print('RESULT:\t', uid_p)

# Search elements whose class contains "class-1" (NOT EXACTLY the whole word)
contains_ex = sel.xpath('//*[contains(@class,"class-1")]').extract()
print('\n4. Search elements whose class contains "class-1" (NOT EXACTLY the whole word):')
print('RESULT:\t', contains_ex)
# COMPARE TO:
# Search any element in all levels whose class is EXACTLY "class-1"
class_ex = sel.xpath('//*[@class="class-1"]')

# Retrieve class attribute value of 2nd paragraph in html/body/div
class_ex2 = sel.xpath('/html/body/div/p[2]/@class').extract()
print('\n5. Retrieve class attribute value of 2nd paragraph in html/body/div:')
print('RESULT:\t', class_ex2)

##### EQUIVALENT SELECTIONS:
div1 = sel.xpath('/html/body/div[1]')
# is the same as
div1 = sel.xpath('/html').xpath('./body/div[1]')
# which is the same as
div1 = sel.xpath('/html').xpath('./body').xpath('./div[1]')
#####

# Text Extraction

# For all elements use: sel.xpath('//p[@id="par"]//text()').extract()
text_p = sel.xpath('//p[@id="par"]/text()').extract() 
print('\nText Extraction:')
print('RESULT:\t', text_p)

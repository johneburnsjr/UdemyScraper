from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re

userSearch = input("Type something to test this out: ")
searchUrl = "https://udemycoupon.learnviral.com/?s="

if userSearch != '':
    r = urllib.request.urlopen(searchUrl + userSearch).read()
else:    
    r = urllib.request.urlopen('https://udemycoupon.learnviral.com/coupon-category/free100-discount/').read()
# multiple clicks r = urllib.request.urlopen('https://www.discudemy.com/category/certification').read()
# multiple clicks r = urllib.request.urlopen('https://udemycoupons.me/').read()


soup = BeautifulSoup(r, "lxml")
pages = soup.find('div', class_='pages')
url = "https://udemycoupon.learnviral.com/coupon-category/free100-discount/page/"
links = pages.find_all('a', class_='page-numbers')

count = 1
for link in links:
    count = count + 1
    newurls = url + str(count)
    print(newurls)
    for site in soup.find_all('a',class_="coupon-code-link btn promotion"):
        
            print(site.get('href'))
            
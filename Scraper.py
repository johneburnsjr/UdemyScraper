#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re
def my_function(x):
  return list(dict.fromkeys(x))

userSearch = input("Enter subject or leave blank to search all ")#get user's input
searchUrl = "https://udemycoupon.learnviral.com/?s=" #default search url

if userSearch != '': #logic to find url based if input is added
    url = 'https://udemycoupon.learnviral.com/page/'
else: 
    url = "https://udemycoupon.learnviral.com/coupon-category/free100-discount/page/"
     

count = 1
for i in range(5):
    count = count + 1
    if userSearch != '': #if user enters string then creates custom URL to scrape
        newurls = url + str(count)+"/?s="+userSearch
    else:
        newurls = url + str(count)
    
    if userSearch != '' and re.search('[1-9,a-z,A-Z]',userSearch):
        r = urllib.request.urlopen(newurls).read()
    elif userSearch == '':    
        r = urllib.request.urlopen(newurls).read()
    else:
        print("Invalid Input")
    # multiple clicks r = urllib.request.urlopen('https://www.discudemy.com/category/certification').read()
    # multiple clicks r = urllib.request.urlopen('https://udemycoupons.me/').read()

    
    soup = BeautifulSoup(r, "lxml") #scrape data
    pages = soup.find('div', class_='pages') #find page divs
    links = pages.find_all('a', class_='page-numbers') #find page numbers in page div   

    for site in soup.find_all('a',class_="coupon-code-link btn promotion"):
         #find coupon code tag and print
            print(site.get('href'))

from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re

r = urllib.request.urlopen('https://udemycoupon.learnviral.com/coupon-category/free100-discount/').read()

soup = BeautifulSoup(r, "lxml")

for link in soup.find_all('a', class_="coupon-code-link btn promotion"):
    print(link.get('href'))
# UdemyScraper
This is my first hands on project to learn Python and Beautiful soup.

##Install Beautiful Soup##
 resource : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

 If you’re using a recent version of Debian or Ubuntu Linux, you can install Beautiful Soup with the system package manager:

$ apt-get install python-bs4 (for Python 2)

$ apt-get install python3-bs4 (for Python 3)

##Making the soup##

To parse a document, pass it into the BeautifulSoup constructor. You can pass in a string or an open filehandle:

from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>a web page</html>")


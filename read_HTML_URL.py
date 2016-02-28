import urllib
from BeautifulSoup import *

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Darya.html"
value = 0

for value in range (0,8):

    print url
    urlFile = urllib.urlopen(url).read()

    soup = BeautifulSoup(urlFile)

    tags = soup("a")

    urlBrowser = tags[17].get("href", None)

    url = urlBrowser

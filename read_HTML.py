import urllib
from BeautifulSoup import *

url = urllib.urlopen(" http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_196958.html").read()
soup = BeautifulSoup(url)
tags = soup("span")

sum = 0
for tag in tags:
    sum += int(tag.contents[0])

print sum

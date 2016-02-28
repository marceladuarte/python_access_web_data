import urllib
import xml.etree.ElementTree as ET

while True:
    url = raw_input('Enter location: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    tree = ET.fromstring(data)

    results = tree.findall('.//count')

    sum = 0
    for result in results:
        sum += int(result.text)

    print sum

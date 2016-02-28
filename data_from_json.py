import urllib
import xml.etree.ElementTree as ET
import json


while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    print 'Retrieving', address
    uh = urllib.urlopen(address)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    info = json.loads(data)

    sum = 0
    for item in info['comments']:
        sum = sum + int(item['count'])

    print sum

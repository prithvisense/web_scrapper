import os
import urlparse
import urllib
import csv
from bs4 import BeautifulSoup
import lxml
mainsite="https://en.m.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)"
rank1=list()
rank2=list()
rank3=list()
htmltext=urllib.urlopen(mainsite).read()
soup= BeautifulSoup(htmltext,"lxml")
i=1
for table in soup.findAll('table',{'class': 'wikitable sortable'}):
    for rank in table.findAll('tr','td').find('a',href=true):
        if(i==1):
            rank1.append(rank.text)
        elif(i==2):
            rank2.append(rank.text)
        else:
            rank3.append(rank.text)
    i=i+1
print(rank1)
print(rank2)
print(rank3)

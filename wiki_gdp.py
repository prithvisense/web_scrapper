import urllib
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
    for rank in table.findAll('a'):
        if rank.text[0] != '[' and rank.text!= 'World':
            if(i==1):
                rank1.append(rank.text.encode('utf-8'))
            elif(i==2):
                rank2.append(rank.text.encode('utf-8'))
            else:
                rank3.append(rank.text.encode('utf-8'))
    i=i+1
total_countries=list(set(rank1+rank2+rank3))
avgrank=list()
for country in total_countries:
    r=list()
    if rank1.count(country)>0:
        r.append(rank1.index(country)+1)
    if rank2.count(country)>0:
        r.append(rank2.index(country)+1)
    if rank3.count(country)>0:
        r.append(rank3.index(country)+1)
    avgrank.append(sum(r)/len(r))
finalrank=list()
for i in range(len(total_countries)):
    finalrank.append(total_countries[avgrank.index(min(avgrank))])
    avgrank[avgrank.index(min(avgrank))]=999
for i in range(len(finalrank)):
	print("["+str(i+1)+"] "+finalrank[i])
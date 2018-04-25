import urllib.request as urllib2
from bs4 import BeautifulSoup
import collections
from datetime import datetime

startTime = datetime.now()
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")

name_question = [] 

for name in soup.find_all('td'):
		name_question.append(name.text)

i=0

l = {}

for name_question in name_question:
	if name_question == '':
		a =1
	else:
		page = urllib2.urlopen(quote_page)
		soup = BeautifulSoup(page, "html.parser")
		name_box  = soup.find_all("td", class_="status_sm")[-1]
		name = name_box.text.replace('\n','')
		l.update({name : name_question})
	i = i+1

od = collections.OrderedDict(sorted(l.items()))

for k, v in od.items():
	print(k, v)

print(datetime.now() - startTime)	#time taken


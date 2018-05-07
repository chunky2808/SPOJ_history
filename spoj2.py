import urllib.request as urllib2
from bs4 import BeautifulSoup
import collections
from datetime import datetime

startTime = datetime.now()
quote_page = "http://www.spoj.com/users/chunky_2808/"
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")

name_question = [] #list of solved problems

for name in soup.find_all('td'):
		name_question.append(name.text)

#as each url has fixed pattern , exploit that property and go to each problem page(open the page) and scrap time of each page in dictonary along with their name

i=0

l = {}

for name_question in name_question:
	if name_question == '':
		a =1
	else:
		quote_page = "http://www.spoj.com/status/%s,chunky_2808//"%name_question
		page = urllib2.urlopen(quote_page)
		soup = BeautifulSoup(page, "html.parser")
		name_box  = soup.find_all("td", class_="statusres text-center")
		
		index = -1
		index2 = 0
		
		for name_box in name_box:
			name = name_box.text.replace('\n','')
			if(name=="accepted"):
				index=0
				index2+=1
		name_box2  = soup.find_all("td", class_="status_sm")
		
		index3=0
		if(index==0):
			for name_box2 in name_box2:
				name2 = name_box2.text.replace('\n','')
				if(index2==index3):
					l.update({name2 : name_question})
					break
				else:
					index3 = index3 + 1	
	i = i+1
#sorted(l, key=l.get)
#sorted(l, key=itemgetter('name', 'age'))
#print(l)

od = collections.OrderedDict(sorted(l.items()))

for k, v in od.items():
	print(k, v)

print(datetime.now() - startTime)	#time taken

#print(od)

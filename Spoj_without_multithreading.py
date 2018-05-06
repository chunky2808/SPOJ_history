import urllib.request as urllib2
from bs4 import BeautifulSoup
import collections
from datetime import datetime

startTime = datetime.now()

quote_page = "http://www.spoj.com/users/chunky_2808/" #Replace it with your user name

page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")

name_question = [] #list of solved problems

#extract name of question from main page of user
for name in soup.find_all('td'):
		name_question.append(name.text)
#extract name of question from main page of user


#as each url has fixed pattern , exploit that property and go to each problem page(open the page) and scrap time of each page in dictonary along with their name
i=0

l = {}


for name_question in name_question:
	# if i ==1:
	# 	break
	if name_question == '':
		a =1
	else:
		quote_page = "http://www.spoj.com/status/%s,chunky_2808//"%name_question #Replace it with your user name
		page = urllib2.urlopen(quote_page)
		soup = BeautifulSoup(page, "html.parser")
		name_box  = soup.find_all("td", class_="status_sm")[-1]
		name = name_box.text.replace('\n','')#time
		l.update({name : name_question})#inserting in list (time of submit ,name of question)
		#print(l)
	i = i+1

od = collections.OrderedDict(sorted(l.items()))

for k, v in od.items():
	print(k, v)


print("Time taken in crawling account")
print(datetime.now() - startTime)	#time taken


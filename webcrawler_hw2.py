# import packages
from bs4 import BeautifulSoup
import urllib.request

# Question 1
## 1.

seed_url = 'https://www.federalreserve.gov/newsevents/pressreleases.htm'
pressrelease_url = 'https://www.federalreserve.gov/newsevents/pressreleases'
urls = []

req = urllib.request.Request(seed_url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib.request.urlopen(req).read()
soup = BeautifulSoup(webpage)
for link in soup.find_all('a'):
	childUrl = link['href']
	o_childurl = childUrl
	childUrl = urllib.parse.urljoin(seed_url, childUrl)
	if pressrelease_url in childUrl and childUrl != seed_url:
		urls.append(childUrl)


covid_urls = []
maxnumber_urls = 10

for url in urls:
	req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urllib.request.urlopen(req).read()
	soup = BeautifulSoup(webpage)
	for link in soup.find_all('a'):
		childUrl = link['href']
		o_childurl = childUrl
		childUrl = urllib.parse.urljoin(seed_url, childUrl)
		if pressrelease_url in childUrl:
			req = urllib.request.Request(childUrl, headers={'User-Agent': 'Mozilla/5.0'})
			webpage = urllib.request.urlopen(req).read()
			soup = BeautifulSoup(webpage)
			if len(covid_urls) >= maxnumber_urls:
				break
			if 'covid' in soup.get_text().lower() and childUrl not in urls and childUrl != seed_url:
				covid_urls.append(childUrl)

print('Number of URLs collected:', len(covid_urls)) # check the length
for covid_url in covid_urls: # check the final output
	print(covid_url)



## 2.

seed_url = 'https://www.sec.gov/news/pressreleases'
core_url = 'https://www.sec.gov/news'
pressrelease_url = 'https://www.sec.gov/news/press-release'
charges_urls = []
maxnumber_urls = 20

req = urllib.request.Request(seed_url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib.request.urlopen(req).read()
soup = BeautifulSoup(webpage)


for link in soup.find_all('a', href = True):
	link = urllib.parse.urljoin(core_url, link['href'])
	if pressrelease_url in link:
		req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urllib.request.urlopen(req).read()
		soup = BeautifulSoup(webpage)
		if len(charges_urls) >= maxnumber_urls:
			break
		if 'charges' in soup.get_text().lower():
			charges_urls.append(link)

print('Number of URLs collected:', len(charges_urls)) # check the length
for charges_url in charges_urls: # check the final output
	print(charges_url)

# End of script
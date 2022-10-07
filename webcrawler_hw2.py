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

print('*****Results for Q1.1 Begin Here*****')
print('Number of URLs collected:', len(covid_urls)) # check the length
for covid_url in covid_urls: # check the final output
	print(covid_url)
print('*****Results for Q1.1 End Here*****')



## 2.

seed_url = 'https://www.sec.gov/news/pressreleases'
core_url = 'https://www.sec.gov/news'
pressrelease_url = 'https://www.sec.gov/news/press-release'
charges_urls = []
charges_texts = []
maxnumber_urls = 20

req = urllib.request.Request(seed_url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib.request.urlopen(req).read()
soup = BeautifulSoup(webpage)


for link in soup.find_all('a', href = True):
	url = urllib.parse.urljoin(core_url, link['href'])
	text = link.text
	if pressrelease_url in url:
		req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urllib.request.urlopen(req).read()
		soup = BeautifulSoup(webpage)
		if len(charges_urls) >= maxnumber_urls:
			break
		if 'charges' in soup.get_text().lower():
			charges_urls.append(url)
			charges_texts.append(text)

print('*****Results for Q1.2 Begin Here*****')
print('Number of URLs collected:', len(charges_urls)) # check the length
for i in range(maxnumber_urls): # check the final output
	print('URL:', charges_urls[i], '\nText:', charges_texts[i], '\n')
print('*****Results for Q1.2 End Here*****')
# End of script
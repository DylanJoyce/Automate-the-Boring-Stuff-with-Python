#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser
fromb s4 import BeautifulSoup

print('Googling...')

res = requests.get('http:google.com/search?q=' + ' '.joain(sys.argv[1:]))
res.raise_for_status

#TODO : Retrive top search result links.
soup = bs4.BeautifulSoup(res.text)

#TODO : Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))
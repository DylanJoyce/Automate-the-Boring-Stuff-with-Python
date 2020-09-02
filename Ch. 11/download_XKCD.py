# download_XKCD.py - 

import requests, os, bs4
#from bs4 import BeautifulSoup

# starting url
url = 'http://xkcd.com'

# store comics in ./xkcd
os.makedirs('xkcd', exist_ok=True)	

while not url.endswith('#'):
	# Find the URL of the comic
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic image.')
	else:
		try:
			comicUrl = 'http:' + comicElem[0].get('src')
			#download the image
			print('Downloading image %s...' %(comicUrl))
			res = requests.get(comicUrl)
		except request.exceptions.MissingSchema:
			# skip this comic
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'http://xkcd.com' + prevLink.get('href')
		#	continue

		# Save the image to ./xkcd
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')

		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()	

	# Get the Prev button's url
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')

	print('Done')

	"""
	USEFUL INFO
	#comic image div
	<div id="comic">
	<img src="//imgs.xkcd.com/comics/cyberintelligence.png" title="We had gathered that raw information, but had yet to put it all together." alt="Cyberintelligence">
	</div>

	#previous button
	<a style="" title="" rel="prev" href="/1572/" accesskey="p">&lt; Prev</a>

	#first comic
	http://xkcd.com/1/#
	"""

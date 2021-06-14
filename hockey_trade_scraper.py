# hockey_trade_scraper

"""
Scrape all the trading data from this website
https://www.capfriendly.com/trades
"""

import os, sys, requests, bs4 # requests and bs4 are not built-in modules

print(50*'*')
print(f'The working directory is: {os.getcwd()}')
print(50*'*', '\n')


url = f'https://www.capfriendly.com/trades'
dir_name = f'file_{url}'

"""
For information on why we need headers see:
https://stackoverflow.com/questions/38489386/python-requests-403-forbidden#:~:text=If%20you%20still%20get%20a,Headers%20of%20the%20Developer%20Tools.
"""
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
res = requests.get(url, headers=headers)


if res.status_code == 404:
	raise SystemExit(f'HTTP response status: {res.status_code}') # Exit with message if URL is bad


soup = bs4.BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())
print(50*'*')
print(soup.get_text())
print(50*'*')
for link in soup.find_all('a'):
	if 'players' in link.get('href'):
		print(link.get('href'))

"""
for link in soup.find(id="div"):
    print(link.get('href'))

players = soup.find_all('/players/jordie-benn')
description = soup.find(property="og:description").get('content')


print(soup)
print(50*'')
print(players)


scraped_stuff2 = soup.find(property="og:description").get('content')
	
with open(f'hockey/{dir_name}/trade_names.txt', 'w') as writer:
	writer.write(description)
"""
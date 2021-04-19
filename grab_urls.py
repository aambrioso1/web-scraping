import os, sys, requests, bs4 # requests and bs4 are not built-in modules

url = 'https://www.mercari.com/u/623628855/'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
res = requests.get(url, headers=headers)

if res.status_code == 404:
	raise SystemExit(f'HTTP response status: {res.status_code}') # Exit with message if URL is bad

soup = bs4.BeautifulSoup(res.text, 'html.parser')

url_list = []
for link in soup.find_all(style="position:relative"):
	if 'us/item' in link.get('href'):
		url_list.append(link.get('href')[10:-1])

print(url_list)


# href="/us/item/m58539546254/" style="position:relative"
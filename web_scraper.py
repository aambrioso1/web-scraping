"""
A web-scraping program for the www.mercari.com website.
See the README file in GitHub for more information:
https://github.com/aambrioso1/web-scraping/blob/master/README.md

usage:  python web_scraper.py FILE_NUM
"""

import os, sys, requests, bs4 # requests and bs4 are not built-in modules

print(50*'*')
print(f'The working directory is: {os.getcwd()}')
print(50*'*', '\n')

# These are the identifcation numbers found on the item urls. 
# For example:  https://www.mercari.com/us/item/m45786125605/
url_num_list = ['94962627845', '28581050712', '45786125605', '59686343331', \
'58539546254', '93471915373', '86489594490', '15676221375', \
'92171004209', '59767956548', '20674928323', '89789051188', \
'61995288639', '80927475884', '96337524430', '56981262426', \
'96138398649', '60372706574', '12850962109', '20217064707', \
'11255445596', '52302814025', '32005985260', '66680840842']

FILE_NUM = int(sys.argv[1])
URL_NUM = url_num_list[FILE_NUM]

url = f'https://www.mercari.com/us/item/m{URL_NUM}/'
dir_name = f'temp{FILE_NUM}'

"""
For information on the need for the headers see:
https://stackoverflow.com/questions/38489386/python-requests-403-forbidden#:~:text=If%20you%20still%20get%20a,Headers%20of%20the%20Developer%20Tools.
"""
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
res = requests.get(url, headers=headers)


if res.status_code == 404:
	raise SystemExit(f'HTTP response status: {res.status_code}') # Exit with message if URL is bad


soup = bs4.BeautifulSoup(res.text, 'html.parser')

img_list = []
for link in soup.find_all('img'):
	if 'photos' in link.get('src'):
		img_list.append(link.get('src'))

print(50*'*')
for i, url in enumerate(img_list):
	print(f'for image{i+1} the url is {url}')
print(50*'*','\n')

print(50*'*')
try:
    # Create the directory dir_name
    os.mkdir(dir_name)
    print(f'Directory {dir_name} created for storing info') 
except FileExistsError:
    print(f'Directory {dir_name} already exists')
print(50*'*')

# We iterate through the image list and save each image in the dir_name folder as image1.jpg, image2.jpg, ...
for i, url in enumerate(img_list):
	res = requests.get(url)
	res.raise_for_status
	# This idea for downloading and image was borrowed from Automate the Boring Stuff.  See README file.
	with open(f'{dir_name}/image' + str(i+1) + '.jpg','wb') as file:
		for chunk in res.iter_content(100000):
			file.write(chunk)

# We save the description in the dir_name folder as description.txt
description = soup.find(property="og:description").get('content')
with open(f'{dir_name}/description.txt', 'w') as writer:
    writer.write(description)

"""
# url = 'https://mercari-images.global.ssl.fastly.net/photos/m45786125605_1.jpg?1617507386'

# The prettify command prints a long, but readable, version of the web page.   
# print(soup.prettify())

# Read through html tags using the inspector in Chrome for a while before I found the right one.

# print(soup.title)
# print("meta stuff", soup.find_all(property="og:image"))

# This is the best way to pull the content from the html.   I use it below for the description variable.
print("description", soup.find(property="og:description").get('content'))

# I used this code to help me find the right stuff.

# creates a list of all the url's on the original html page
url_list = []
for link in soup.find_all(property="og:image"):
	url_list.append(link.get('content'))

print(url_list)

for i, url in enumerate(url_list):
	res = requests.get(url)
	res.raise_for_status
	file = open('images/image' + str(i) + '.jpg','wb')
	for chunk in res.iter_content(100000):
		file.write(chunk)
	file.close()

# Prints out a the p tag stuff
for stuff in soup.find_all('p'):
	print(stuff.get('class'))  # "Text-uqn6ov-0 Text__T2-uqn6ov-10 Spec__Description-sc-1oxis5o-6 jyCFdx"

This is code I wrote to try to figure out the best way to pull the info from the html
for i, text in enumerate(soup.find_all('meta')):
	print(i+1, text.get('property'))
	if text.get('property')  == 'og:description':
		print(text.get('content'))

for text in soup.find_all('meta'):
	if text.get('property')  == 'og:description':
		description = text.get('content')
		print(description)
"""
"""
['94962627845', '28581050712', '45786125605', '59686343331', 
'58539546254', '93471915373', '86489594490', '15676221375', 
'92171004209', '59767956548', '20674928323', '89789051188', 
'61995288639', '80927475884', '96337524430', '56981262426', 
'96138398649', '60372706574', '12850962109', '20217064707', 
'11255445596', '52302814025', '32005985260', '66680840842']
"""
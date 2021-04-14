import requests, os, bs4, sys

print('\n', 50*'*')
print(f'The working directory is: {os.getcwd()}')
print(50*'*', '\n')
# print('\n')

url = 'https://www.mercari.com/us/item/m45786125605/'

"""
For information on the need for the headers see:
https://stackoverflow.com/questions/38489386/python-requests-403-forbidden#:~:text=If%20you%20still%20get%20a,Headers%20of%20the%20Developer%20Tools.
"""

"""
# One way to check of arguments
try:
    arg = sys.argv[1]
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <URL>")
"""

if len(sys.argv) == 1:
	url = 'https://www.mercari.com/us/item/m45786125605/'
else:
	url = sys.argv[1]



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
print(50*'*')

for i, url in enumerate(img_list):
	res = requests.get(url)
	res.raise_for_status
	# This code was borrowed from Automate the Boring Stuff.  May want to refactor using a with statement.
	file = open('images/image' + str(i+1) + '.jpg','wb')
	for chunk in res.iter_content(100000):
		file.write(chunk)

	file.close()

description = soup.find(property="og:description").get('content')

with open('description/description.txt', 'w') as writer:
    writer.write(description)


# url = 'https://mercari-images.global.ssl.fastly.net/photos/m45786125605_1.jpg?1617507386'

# Prints a long, but readable, version of the web page.   
# Please create this document as a text file and send it to me.
# print(soup.prettify())

# Had to dig through div tags using the inspector for a while before I found the right one.
"""
text_tag = '#__next > div.Flex-ych44r-0.Space-cutht5-0.Container-sc-9aa7mx-0.ieZXaq.' \
    'Layout__HeaderPlaceholder-sc-113qaek-3.dUbAPb > div.BodyContainer__ResponsiveContainer' \
    '-sc-1iymb8v-2.ItemDesktop__BodyWrapper-sc-1yqibs5-0.bMJlQC > div:nth-child(2) > ' \
    'div.Flex-ych44r-0.Space-cutht5-0.Container-sc-9aa7mx-0.ItemDesktop__RightColumn-sc-1yqibs5-2.byDGRF > ' \
    'div.Section-sc-694wzh-0.eymcbl > div > p.Text-uqn6ov-0.Text__T2-uqn6ov-10.Spec__Description-sc-1oxis5o-6.jyCFdx'
text_tag2 = ''

text = soup.select(text_tag)
text_string = str(text)

if text == []:
        print('Could not find text.')
else:
    print(f'text is {text}')
    with open('erika_file', 'w') as writer:
    	writer.write(soup.prettify())

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
"""


"""
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
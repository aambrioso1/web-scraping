# A script, get_url_text.py to download the html source at a URL to a text file to a folders
# call url_text

# Usage get_url_text.py url foldername filename

import os, sys, requests, bs4

print(f"{sys.argv=}")

url = sys.argv[1]
foldername = sys.argv[2]
filename = sys.argv[3]

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
res = requests.get(url, headers=headers)
if res.status_code == 404:
	raise SystemExit(f'HTTP response status: {res.status_code}') # Exit with message if URL is bad

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# text1 = soup.prettify()
text = soup.prettify()

"""
try:
    os.remove(foldername)
except OSError as e:  ## if failed, report it back to the user ##
    print (f'Error: {e.filename} - {e.strerror}')
"""

os.mkdir(foldername)

with open(f'{foldername}/{filename}', 'w', encoding='utf-8') as writer:
    writer.write(text)

"""
for https://www.gutenberg.org/ the code causes the following error:

Traceback (most recent call last):
  File "get_url_text.py", line 33, in <module>
    writer.write(text)
  File "C:\Program Files\Python38\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\u25be' in position 1885: character maps to <undefined>
"""



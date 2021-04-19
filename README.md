# web-scraping
A repository for experiments in web-scraping.

web_scraper
***********************************************************************

Usage:  web_scraper optional <FILE_NUM> 

If URL and dir_name are both missing https://www.mercari.com/us/item/m{URL_NUM}/ and /temp are used.
If the dir_name is missing then /temp is used.
If a bad URL is given the program exits with the message:  
HTTP response status:  <status code>
if only a dir_name is given then likely the program will exit with an HTTP response status unless
the dir_name happens to be a URL.

This program grabs the description and stuff toy images from URL for www.mercari.com
and posts them to the host computer's hard drive in a folder called dir_name.    
The program also prints the current working directory and the the URLs for the images that are downloaded.

The description and the images are placed in a file named temp{FILE_NUM}.

It requires two modules that are not built-in to Python: requests and beautiful soup.
Requests is used to manage the http requests, The built-in module urllib3 will handle http requests but
it is difficult to use.   Beautiful soup is used to parse the html.   Both requests and beautiful have
excellent online documentation.

The idea for this program was inspired by Al Sweitgart's nice book 
Automate the Boring Stuff (Chapter 12).

This are the numbers that identify the URLS to be scraped.
url_num_list = ['94962627845', '28581050712', '45786125605', '59686343331', \
'58539546254', '93471915373', '86489594490', '15676221375', \
'92171004209', '59767956548', '20674928323', '89789051188', \
'61995288639', '80927475884', '96337524430', '56981262426', \
'96138398649', '60372706574', '12850962109', '20217064707', \
'11255445596', '52302814025', '32005985260', '66680840842']

Other files
***********************************************************************
erika_file: a text file with all the html on the page at the URL listed above.
The code to generate this file is commented out in the program.
temp files:   These files contain the description and images for different pages.

TODO
***********************************************************************
Need to settle on a final design:
(1)  Two module one for downloading descriptions and one for downloading images.
(2)  What functionality will work best.

Nice article on command line arguments in Python: https://realpython.com/python-command-line-arguments/
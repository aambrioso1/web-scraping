# web-scraping
A repository for experiments in web-scraping.

web_scraper
***********************************************************************

Usage:  web_scraper optional <URL> optional: <dirName>
If URL and dirName are both missing https://www.mercari.com/us/item/m45786125605/ and /temp are used.
If the dirName is missing then /temp is used.
If a bad URL is given the program exits with the message:  
HTTP response status:  <status code>
if only a dirName is given then likely the program will exit with an HTTP response status unless
the dirName happens to be a URL.

This program grabs the description and stuff toy images from URL for www.mercari.com
and posts them to the host computer's hard drive in a folder called dirname.    The program also prints the current working directory 
and the the URLs for the images that are downloaded.

It requires two modules that are not built-in: requests and beautiful soup.
The idea for this program was inspired by Al Sweitgart's nice book 
Automate the Boring Stuff (Chapter 12).



Other files
***********************************************************************
erika_file: a text file with all the html on the page at the URL listed above.
The code to generate this file is commented out in the program.

TODO
***********************************************************************
I would like be able to adapt the program to take a list of Mercari URL's and write 
requested text or images to the host computers hard drive.

Need to try the current program with different URLs.

Nice article on command line arguments in Python: https://realpython.com/python-command-line-arguments/
# web-scraping
A repository for experiments in web-scraping.

web_scraper
***********************************************************************
This program grabs the description and stuff toy images from the website:
https://www.mercari.com/us/item/m45786125605/
and posts them to the host computer's hard drive in folders called description
and images respectively.    The program also prints the URLs for the images
that are downloaded by it.

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
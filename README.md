### web-scraping  
A repository for experiments in web-scraping.

**web_scraper.py**   
Usage:  web_scraper.py FILE_NUM 
The script goes to  https://www.mercari.com/us/item/m{URL_NUM}/ downloads the merchandise
decription text and all the images into the folder called /temp{FILE_NUM}.   URL_NUM corresponds
to url_id_list[FILE_NUM] in the list below.

This program grabs the description and images from URL for mrechandise on www.mercari.com.   
The description and the images are placed in a file named temp{FILE_NUM}.      
The program also prints the current working directory and the the URLs for the images that are downloaded.   


It requires two modules that are not built-in to Python: requests and beautiful soup.    
Requests is used to manage the http requests. The built-in module urllib3 will handle http requests but it is difficult to use.   Beautiful soup is used to parse the html.  Both requests and beautiful soup have    
excellent online documentation.   See notes below.    

The script grab_urls.py identifies the URLs that need to be scraped.   

Using this script the following ID numbers identify the URLS to be scraped.   
url_id_list = ['94962627845', '28581050712', '45786125605', '59686343331', \
'58539546254', '93471915373', '86489594490', '15676221375', \
'92171004209', '59767956548', '20674928323', '89789051188', \
'61995288639', '80927475884', '96337524430', '56981262426', \
'96138398649', '60372706574', '12850962109', '20217064707', \
'11255445596', '52302814025', '32005985260', '66680840842']

**Other files**   
grab_urls.py        
Identifies URLs that need to be scraped.

get_url_text.py    
Usage get_url_text.py url foldername filename 
Saves the HTML for the page at url as /foldername/filename.txt in the current working directory.

erika_file    
A text file with all the html on the page at the URL associate with the ID '45786125605'.
The code to generate this file is commented out in the file.

temp files    
These files contain the description and images from several different pages.



**TODO**   
(1)  Need to settle on a final design.  
(2)  What functionality will work best.   Create scripts to access this functionality.
(3)  Two modules for downloading information one for descriptions and one for downloading images.
(4)  Need to download dates when info is posted to decide when it should be re-posted.

*********************************************************************************************
**Notes**   
The idea for this code was inspired by Al Sweitgart's nice book: https://automatetheboringstuff.com/2e/chapter12/
This is a nice article on command line arguments in Python from Real Python:
https://realpython.com/python-command-line-arguments/
These two libraries have excellent documentation:
Beautiful Soup:  https://www.crummy.com/software/BeautifulSoup/bs4/doc/
Requests:  https://docs.python-requests.org/en/master/
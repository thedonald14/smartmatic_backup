import pandas as pd
import urllib.request
from urllib.parse import urlparse

def dlsmartmaticsite():
    """This program downloads all HTML files from a Linkchecker Site Crawl.
        
        To crawl the site linkchecker was used. And can be installed here :
        pip3 install git+https://github.com/linkchecker/linkchecker.git
        
        To run the Crawl use :
        linkchecker -v -o csv https://www.smartmatic.com/us/ > smartmatic.csv
        this  will export the file that is needed below.
        
        """
    
    df = pd.read_csv("smartmatic.csv",skiprows=3,error_bad_lines=False,delimiter=";")
    listofurls = [url for url in df.url if not str(url).endswith(("jpg","png",".pdf",".js"))]

    for url in listofurls: 
        try:
            urlname = urlparse(url).path
            
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            html = urllib.request.urlopen(req).read()
             
            with open(f'smartmaticsite/{urlname.replace("/","")}.txt', 'w') as file:
                file.write(str(html))
                print(f"Wrote to File for {urlname}") 
        
        except Exception as e: 
            print(e)
            pass
    
if __name__ == "__main__":
    dlsmartmaticsite()

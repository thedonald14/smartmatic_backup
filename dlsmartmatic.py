import pandas as pd
import urllib.request
from urllib.parse import urlparse
import os

def dlsmartmaticsite():
        """
        This program downloads all HTML files from smartmatic.com from a Linkchecker Site Crawl.
        
        To crawl the site linkchecker was used. And can be installed here :
        pip3 install git+https://github.com/linkchecker/linkchecker.git
        
        To run the Crawl use :
        linkchecker -v -o csv https://www.smartmatic.com/us/ > smartmatic.csv
        this  will export the file that is needed below.
        
        To view the text for each file, without HTML use:
        pip3 install html2text
        html2text(filename.text)
        
        """
    # Read all urls into a pandas DataFrame.
    df = pd.read_csv("smartmatic.csv",skiprows=3,error_bad_lines=False,delimiter=";")
        
    # Remove non HTML links from Dataframe and make list of URL only.
    #TODO Find and remove additional non HTML Pages like "JPEG"
    listofurls = [url for url in df.url if not str(url).endswith(("jpg","png",".pdf",".js"))]
    
    if not os.path.exists('smartmaticsite'):
        os.makedirs('smartmaticsite')
        
    for url in listofurls: 
        try:
            # Get name of link for file save.
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
                    
# A Production of the Patriotic Deep State.
# print(f"{chr(21328)}")

import os
import urllib.request
import sys
from bs4 import BeautifulSoup


dirs = os.listdir("./")
page_count = 0

for i in dirs:
    pages = os.listdir("./"+i)
    for j in pages:
        with open("./"+i+"/"+j) as s:
            content = s.read()
            soup = BeautifulSoup(content, 'html.parser')
            gr = soup.find_all("div","g")
            for g in gr:
                page_title = g.find_all("div","st")[0]
                page_link = g.find_all("a")[0].get("href")

                try:
                    req = urllib.request.Request(
                        page_link, 
                        data=None, 
                        headers={
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                                }
                    )

                    webf = urllib.request.urlopen(req)
                    link_content = webf.read()
                   
                    link_html = BeautifulSoup(link_content, 'html.parser')
                    result = ""
                    if "https://udn.com" in page_link:
                        link_html_body = link_html.find(id="story_body_content")
                        children = link_html_body.findChildren("p" , recursive=True)
                        for child in children:
                            result = result+str(child)
                        #print(result)
        
                    
                    elif "www.thenewslens.com" in page_link:
                        link_html_body = link_html.find_all("article")
                        children = link_html_body[0].findChildren("p" , recursive=True)
                    
                        for child in children:
                            result = result+str(child)
                            #print(child)
                        #print(result)
                        
                        
                    
                    elif "yahoo.com" in page_link:
                        soup = BeautifulSoup(link_content, 'html.parser')
                        link_html_body = soup.select("p.canvas-atom")
                        #link_html_body = link_html.find_all("class","canvas-atom")
                        #print(link_html)
                       
                        for child in link_html_body:
                            result = result+str(child)
                        #print(result)
                        
                    
                    elif "stars.udn.com" in page_link:
                   
                        link_html_body = link_html.select("div#story")
                        #print(link_html)
                       
                        for child in link_html_body:
                            
                            result = result+str(child)
                            
                        #print(result)
                        
                        
                    elif "dwnews.com" in page_link:
                        link_html_body = link_html.select("div.container")
                        
                        children = link_html_body[0].findChildren("div" , recursive=True)
                        print(len(link_html_body))
                        for child in children:
                            result = result+str(child)
                            
                            
                        #print(result)
                    
                    elif "cna.com.tw" in page_link:
                        link_html_body = link_html.select("div.paragraph")
                        children = link_html_body[0].findChildren("p" , recursive=True)
                        for child in children:
                            result = result+str(child)
                
                        #print(result)
                    
                    
                    elif "storm.mg" in page_link:
                        #print("====");
                        #print(page_link)
                        link_html_body = link_html.select("article")
                        children = link_html_body[0].findChildren("p" , recursive=True)
                        for child in children:
                            result = result+str(child)
                
                        #print(result)
                    
                    
                    elif "news.tvbs.com" in page_link:
                        #print("====");
                        #print(page_link)
                        link_html_body = link_html.select("div#news_detail_div")
                        
                        for child in link_html_body:
                            result = result+str(child)
                
                        #print(result)
                    
                    elif "game.ettoday.net" in page_link:
                        #print("====");
                        #print(page_link)
                        link_html_body = link_html.select("div.story")
                        children = link_html_body[0].findChildren("p" , recursive=True)
                        for child in link_html_body:
                            result = result+str(child)
                
                        #print(result)
                    
                    
                    elif "koreastardaily.com" in page_link:
                        #print("====");
                        #print(page_link)
                        link_html_body = link_html.select("div#content-body")
                        children = link_html_body[0].findChildren("p" , recursive=True)
                        for child in link_html_body:
                            result = result+str(child)
                
                        #print(result)
                    
  
                    
                    elif "www.epochtimes.com" in page_link:
                        #print("====");
                        #print(page_link)
                        link_html_body = link_html.select("div#artbody")
                        children = link_html_body[0].findChildren("p" , recursive=True)
                        for child in link_html_body:
                            result = result+str(child)
                
                        #print(result)
                    
                    

                    
                    else:
                    
                        print("====");
                        print(page_link)
                    
                    page_count = page_count + 1
                        
                        
                except:
                    print("error")
                    print(sys.exc_info())
                    print(page_link)
                    raise
                    
                    
print(page_count)
         

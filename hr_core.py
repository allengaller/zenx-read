# Allen Galler
# allengaller@gmail.com

import urllib2, webbrowser, os, re
from HTMLParser import HTMLParser

hacker_news_url = "http://news.ycombinator.com/"

request = urllib2.Request(hacker_news_url)
response = urllib2.urlopen(request)
buffer = response.read()

# Parse links from the mainpage.
class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for (variable, value) in attrs:
                    if variable == "href": self.links.append(value)

        return self.links

# Clean up link list and run.
def Runner(raw_url_list):
    clean_url_list = []
    
    for raw_url in raw_url_list:
        if raw_url.find("http") ==0:
            if raw_url.find("http://ycombinator.com") != 0:
                #print raw_url
                webbrowser.open(raw_url)
    return clean_url_list       
                   
if __name__ == "__main__":
    hacker_parser = Parser()
    hacker_parser.feed(buffer)

    clean_list = Runner(hacker_parser.links)
    
    hacker_parser.close()


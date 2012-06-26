#This is the core function in Python.

import urllib2, webbrowser, os
from HTMLParser import HTMLParser

hacker_url = "http://news.ycombinator.com/"

request = urllib2.Request(hacker_url)
response = urllib2.urlopen(request)
buffer = response.read()

class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
 
    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "href":
                        self.links.append(value)

if __name__ == "__main__":
    hacker_parser = Parser()
    hacker_parser.feed(buffer)

    for items in hacker_parser.links:
        if items.find("http") == 0:
            print items
            webbrowser.open(items)

    hacker_parser.close()
    

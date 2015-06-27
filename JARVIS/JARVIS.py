#coding=utf-8
##urllib2 documentation at "https://docs.python.org/2/library/urllib2.html"
#Requirements:
#1 Get all file path

import urllib.request
import urllib.error
import 
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
html = getHtml("http://www.jd.com")

fin = open("temp.txt",'w')
fin.write(str(html))
fin.close()


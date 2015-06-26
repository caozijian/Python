#coding=utf-8
##urllib2 documentation at "https://docs.python.org/2/library/urllib2.html"
import urllib.request
import urllib.error

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
html = getHtml("http://www.cpsri.com.cn")
fin = open("temp.txt",'w')
fin.write(str(html))
fin.close()


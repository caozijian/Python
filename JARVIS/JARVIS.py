#coding=utf-8
##urllib2 documentation at "https://docs.python.org/2/library/urllib2.html"
#Requirements:
#1 Get all file path
##0629 so tired.today
import urllib.request
import urllib.error
import re


def getHtml(url):
    headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20141127 Firefox/2.0.0.11'}
    #req = urllib.request(url=url,headers=headers)
    page = urllib.request.urlopen(url)
    print(page.info())
    raw_html = page.read()
    html = raw_html.decode("utf-8")
##    print(raw_html)
    return html

html = getHtml("http://www.python.org")

def getImg(html):
    reg = r'href="(.+?\.css)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

print(getImg(html))

fin = open("temp.txt",'w')
fin.write(str(html))
fin.close()


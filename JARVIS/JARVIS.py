#coding=utf-8
##urllib2 documentation at "https://docs.python.org/2/library/urllib2.html"
#Requirements:
#1 Get all file path
##0629 so tired.today
##Get two type of file list
##Seperate pattern expression.
import urllib.request
import urllib.error
import re


def getHtml(url):
    headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20141127 Firefox/2.0.0.11'}
    #req = urllib.request(url=url,headers=headers)
    page = urllib.request.urlopen(url)
##    print(page.info())
    raw_html = page.read()
    html = raw_html.decode("utf-8")
##    print(raw_html)
    return html

def getRef(html):
##Python regular expression
##The special characters are:
##    '.'(Dot.) In the default mode, this matches any character except a newline. If the DOTALL flag has been specified, this matches any character including a newline.
##    '^'(Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.
##    '$'Matches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline. foo matches both ‘foo’ and ‘foobar’, while the regular expression foo$ matches only ‘foo’. More interestingly, searching for foo.$ in 'foo1\nfoo2\n' matches ‘foo2’ normally, but ‘foo1’ in MULTILINE mode; searching for a single $ in 'foo\n' will find two (empty) matches: one just before the newline, and one at the end of the string.
##    '*'Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible. ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.
##    '+'Causes the resulting RE to match 1 or more repetitions of the preceding RE. ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.
##    '?'Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’.*?, +?, ??The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible. Sometimes this behaviour isn’t desired; if the RE <.*> is matched against '<H1>title</H1>', it will match the entire string, and not just '<H1>'. Adding '?' after the qualifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched. Using .*? in the previous expression will match only '<H1>'.

# 
# Seperate a reg expression into multi part. You can even get extention file name list from a file.
##May href is hyper ref?
##You can get the list from a file.
    reglist = ['css','js']
##    reg = r'^href="(.+?\.'
    # try to modify the regx to get new result.
    reg = r'href="(.+?\.css)"'
    
##    for i in range(len(reglist)-1):
##         reg = reg + reglist[i] + ')|(.+?\.'
##    reg += reglist[i+1]
##    reg += ')"'
##    reg += '|(.+?\.js)"'
##    print(reg)
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

## This function get ref file path from a web page.
def getRefFile(url):
    html = getHtml(url)
    for each_item in getImg(html):
        print(each_item)
        
def getBusSchedule():
    headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20141127 Firefox/2.0.0.11'}
    url = "http://wap.ksbus.com.cn/lineGps/843/upOrDown/0/station/-1/order/-1"
    page = urllib.request.urlopen(url)
    raw_html = page.read()
    html = raw_html
    print(html)

getBusSchedule()

##fin = open("temp.txt",'w')
##fin.write(str(html))
##fin.close()


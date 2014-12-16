#!/usr/bin/python
from sgmllib import SGMLParser  
import urllib2
import BeautifulSoup

def catch_a_page(url):

    req = urllib2.Request(url)
    try:
        response = urllib2.urlopen(req)
    except:
        print "error"
    page = response.read()
    return page

def parse_page(bbs_html):
    soup = BeautifulSoup.BeautifulStoneSoup(bbs_html)
    soup = soup.findAll("div")
    count = 0
    result = {}
    add_v = ""
    add_k = ""
    for data in soup:
        value = data.find("a")
        if not value:
            continue
        str_data = str(data)
        if str_data[0:5] != "<div>":
            continue
        if not count % 2:
            add_k = str_data.split("\"")[1]
            add_v = str_data.split(">")[2].split("<")[0]
        else:
            add_v += "===="
            add_v += str_data[5:15]
            add_v += "===="
            add_v += str_data.split(">")[2].split("<")[0]
            result[add_k] = add_v
        count += 1
    return result

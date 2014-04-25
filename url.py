from __future__ import division
import urllib2
import urllib
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import sys
import time


input = "2 States"
input = input.lower()
input = input.split(" ")
input = "-".join(input)

# print "http://songs.pk/indian-mp3-songs/{}-2014-mp3-songs.html".format(input)
url = "http://songs.pk/indian-mp3-songs/{}-2014-mp3-songs.html".format(input)
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)
links = soup.find_all("a")

def top_movies():
    soupstrainer = SoupStrainer("a")
    page = urllib2.urlopen("http://songs.pk/")
    soup = BeautifulSoup(page , "html.parser" , parse_only = soupstrainer)

    for link in soup:
        try:
            if "indian-mp3-songs" in link["href"]:
                print link
            
        except KeyError:
            pass
        # if "songid" in link.href:
        #   print link

def reporthook(a,b,c): 
    # ',' at the end of the line is important!
    print "% 3.1f%% of %d bytes\r" % (min(100, float(a * b) / c * 100), c),
    sys.stdout.flush()

def download(links):
    for link in links:
        try:
            if "song1.php?songid" in link["href"]:
                print (link["href"] , "{}.mp3".format(link.string))
                print urllib.urlretrieve(link["href"], "{}.mp3".format(link.string) , reporthook )
             
        except KeyError:
            pass
        # if "songid" in link.href:
        #   print link
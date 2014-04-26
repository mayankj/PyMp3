from __future__ import division
import urllib2
import urllib
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import sys
import time

def show_songs(songs):
    print "The songs are - "
    for song in songs:
        print song[1]
    confirm = raw_input("Download ? (Press Y or N) ")
    if confirm == "Y" or confirm == "y" or confirm == "yes" or confirm == "Yes":
        for song in songs:
            print song[1]
            urllib.urlretrieve(song[0], "{}.mp3".format(song[1]) , reporthook )


def reporthook(a,b,c): 
    # ',' at the end of the line is important!
    print "% 3.1f%% of %d bytes\r" % (min(100, float(a * b) / c * 100), c),
    sys.stdout.flush()

def get_songs(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    links = soup.find_all("a")
    songs = []
    for link in links:
        try:
            if "song1.php?songid" in link["href"]:
                songs.append((link["href"],link.string))
                # print urllib.urlretrieve(link["href"], "{}.mp3".format(link.string) , reporthook )
        except KeyError:
            pass
    show_songs(songs)

def top_movies():
    soupstrainer = SoupStrainer("a")
    page = urllib2.urlopen("http://songs.pk/")
    soup = BeautifulSoup(page , "html.parser" , parse_only = soupstrainer)

    for link in soup:
        try:
            if "indian-mp3-songs" in link["href"]:
                print link.contents[0].string 
            
        except KeyError:
            pass
        # if "songid" in link.href:
        #   print link

def get_link(links):
    count = 0
    found = False
    for link in links:
        if "mp3-songs" in link["href"] and count < 1:
            confirm = raw_input("Confirm link to get_songs from - \n{} \nPress Y or N - ".format(link["href"]))
            if confirm == "Y" or confirm == "y" or confirm == "yes" or confirm == "Yes":
                get_songs(link["href"])
                found = True
            else:
                "Aborting"
            count += 1
            # print (link["href"] , "{}.mp3".format(link.string))
            # print urllib.urlretrieve(link["href"], "{}.mp3".format(link.string) , reporthook )
    if found ==  False: print "Incorrect spelling/Does not exist :( "    
   
        # if "songid" in link.href:
        #   print lin

def start():
    input = raw_input("Enter the name of movie - ")
    input = input.lower()
    input = input.split(" ")
    input = "+".join(input)

    # print "http://songs.pk/indian-mp3-songs/{}-2014-mp3-songs.html".format(input)
    url = "http://www.google.com/cse?cx=partner-pub-2959483402321730:5602613899&ie=UTF-8&q={}&sa=Search&siteurl=songsmusic.in&nojs=1".format(input)
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    page = urllib2.urlopen(req)

    soup = BeautifulSoup(page)
    links = soup.find_all("a" , limit = 10)

    get_link(links)

start()
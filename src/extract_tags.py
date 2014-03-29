#!/usr/bin/env python

import re

# this regex should work across most/all video pages
artistTitleRegex = '''(data-video-title</span>="<span class="webkit-html-attribute-value">)(.+?)( - )(.+?)(?:<)'''

# channel will be known by program
channel  = '''AirwaveDubstepTV'''

def GetSongData( video_page, videopage_regex):
    '''given youtube video page html text, returns artist and title'''
    pdata = re.search(videopage_regex, video_page)
    if pdata:
        return (pdata.group(2), pdata.group(4))
    else:
        return ("Error", "GetSongData")

# BEGIN MAIN

# open a sample html file
page_text = open("videoADT.html", "r").read()

# run extration
(artist, title) = GetSongData( page_text, artistTitleRegex)

print "artist  = " + artist 
print "title   = " + title 
print "channel = " + channel 


#!/usr/bin/env python

import re

artistTitleRegex = '''(<span class="webkit-html-attribute-name">data-video-title</span>="<span class="webkit-html-attribute-value">)(.+?)( - )(.+?)(?:</span>)'''

name    = '''AirwaveDubstepTV'''

def GetSongData( video_page, videopage_regex, channel_name):
    pdata = re.search(videopage_regex, video_page)
    if pdata:
        return (pdata.group(2), pdata.group(4), channel_name)

page_text = open("videoADT.html", "r").read()

(artist, title, channel) = GetSongData( page_text, artistTitleRegex, name)

print "artist  = " + artist 
print "title   = " + title 
print "channel = " + channel 


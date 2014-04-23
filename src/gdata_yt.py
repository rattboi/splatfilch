# http://developers.google.com/youtube/1.0/developers_guide_python#RetrievingVideos
# These haven't been changed from this source
# There are errors with the location but it still pulls the recently added videos when tested
# Need to import the gdata package

import gdata.youtube
import gdata.youtube.service
import json

yt_service = gdata.youtube.service.YouTubeService()
# Issue #21 and 19, maybe 20?
# TODO: Read from file, search channel, output urls to file
# output names, channels, more...?
# issue 6 deals with crontab.  Make branch, upload file and list instrucctions.  Where to save it?
#This function gets the user (channel) and prints the video title, description, url, etc


def main():
    f = open('channels.txt', 'r')
    lines = f.readlines()
    f.close()
    for l in lines:
        SearchAndPrint(l[:-1])


def SearchAndPrint(user):
    yt_service = gdata.youtube.service.YouTubeService()
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.time = 'today'
    query.author = user 
    query.max_results = 10
    query.orderby = 'viewCount'
    query.racy = 'include'
    feed = yt_service.YouTubeQuery(query)
    #print feed.media.player.url
    PrintVideoFeed(feed)
  

def PrintEntryDetails(entry):
    print 'Video title: %s' % entry.media.title.text
    print 'Video published on: %s ' % entry.published.text
    print 'Video description: %s' % entry.media.description.text
    print 'Video category: %s' % entry.media.category[0].text
    print 'Video tags: %s' % entry.media.keywords.text
    print 'Video watch page: %s' % entry.media.player.url
    print 'Video flash player URL: %s' % entry.GetSwfUrl()
    print 'Video duration: %s' % entry.media.duration.seconds


def PrintVideoFeed(feed):
    for entry in feed.entry:
        PrintEntryDetails(entry)

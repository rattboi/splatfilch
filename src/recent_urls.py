import gdata.youtube
import gdata.youtube.service
import json
              
# To run, install the gdata package
# Go to https://code.google.com/p/gdata-python-client/downloads/list and download the gdata library
# Unzip and run 'setup.py install' in the gdata directory
# Code used here is referenced/taken from http://developers.google.com/youtube/1.0/developers_guide_python#RetrievingVideos

# TODO: Installation automation in script 
# This program gets users (channels) from 'channels.txt', finds the recently uploaded songs, and saves the
# channel, title, and URL to another file, 'URLs.txt'. 
def main():
    # open file containing selected channels to search through
    f = open('channels.txt', 'r')
    lines = f.readlines()
    f.close()
    # for each line (which corresponds to user)
    for user in lines:
         SearchAndPrint(user.rstrip()) # send user with '\n' removed

  
def SearchAndPrint(user):
    '''Queries from the gdata api to specific search parameters'''
    # This looks for any videos uploaded today based on the user (channel)
    yt_service = gdata.youtube.service.YouTubeService()
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.time = 'today'
    query.author = user
    # Max results limits # of results we look at, can be changed accordingly
    query.max_results = 25 
    query.orderby = 'viewCount'
    query.racy = 'include'
    feed = yt_service.YouTubeQuery(query)
    # print to console to verify - not needed in the future
    PrintVideoFeed(feed)
    for entry in feed.entry:
        SaveURL(entry, user)
 
    
def PrintEntryDetails(entry):
    print 'Video title: %s' % entry.media.title.text
    print 'Video watch page: %s' % entry.media.player.url

def PrintVideoFeed(feed):
    for entry in feed.entry:
        PrintEntryDetails(entry)

def SaveURL(entry, user):
    '''Saves information to a file with the format  Channel,URL,title\n
    No spaces are after the commas.'''
    f = open("URLs.txt", "a")
    url = entry.media.player.url
    title = entry.media.title.text
    # do partition when '&' is spotted
    # should make sure '&' doesn't appear normally
    url = url.partition('&')[0]
    f.write(user + ',' + url + ',' + title + '\n')
    f.close
	 
def read_URLS():
    '''Sample function for how to read files with song information'''
    f = open('URLs.txt', 'r')
    lines = f.readlines()
    f.close()
    # To split the entry, partition based on the ','
    # Note there are now 3 fields -- Channel, URL, title
    lines[0].partition(',')[0]
    # To get rid of '\n', use .rstrip()
    # Do what you want after this ...    


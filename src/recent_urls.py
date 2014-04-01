# http://developers.google.com/youtube/1.0/developers_guide_python#RetrievingVideos
# Need to import the gdata package
        
import gdata.youtube
import gdata.youtube.service
import json
              
# Issue #21 and 19, maybe 20?
# issue 6 deals with crontab.  Make branch, upload file and list instrucctions.
#This function gets the user (channel) and prints the video title, description,

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
    PrintVideoFeed(feed)
 
 
def PrintEntryDetails(entry):
    print 'Video title: %s' % entry.media.title.text
    print 'Video watch page: %s' % entry.media.player.url

def PrintVideoFeed(feed):
    for entry in feed.entry:
        PrintEntryDetails(entry)
	SaveURL(entry)

def SaveURL(entry):
    f = open("URLs.txt", "a")
    # do partition when '&' is spotted and remove 
    f.write(entry.media.player.url)
    f.write('\n')
    f.close()
	 

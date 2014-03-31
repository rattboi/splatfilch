# http://developers.google.com/youtube/1.0/developers_guide_python#RetrievingVideos
# These haven't been changed from this source
# There are errors with the location but it still pulls the recently added videos when tested


def PrintVideoFeed(feed):
  for entry in feed.entry:
    PrintEntryDetails(entry)

def GetAndPrintVideoFeed(uri):
  yt_service = gdata.youtube.service.YouTubeService()
  feed = yt_service.GetYouTubeVideoFeed(uri)
  for entry in feed.entry:
    PrintEntryDetails(entry)

def PrintEntryDetails(entry):
  print 'Video title: %s' % entry.media.title.text
  print 'Video published on: %s ' % entry.published.text
  print 'Video description: %s' % entry.media.description.text
  print 'Video category: %s' % entry.media.category[0].text
  print 'Video tags: %s' % entry.media.keywords.text
  print 'Video watch page: %s' % entry.media.player.url
  print 'Video flash player URL: %s' % entry.GetSwfUrl()
  print 'Video duration: %s' % entry.media.duration.seconds

  # non entry.media attributes
  print 'Video geo location: %s' % entry.geo.location()
  print 'Video view count: %s' % entry.statistics.view_count
  print 'Video rating: %s' % entry.rating.average

  # show alternate formats
  for alternate_format in entry.media.content:
    if 'isDefault' not in alternate_format.extension_attributes:
      print 'Alternate format: %s | url: %s ' % (alternate_format.type,
                                                 alternate_format.url)

  # show thumbnails
  for thumbnail in entry.media.thumbnail:
    print 'Thumbnail url: %s' % thumbnail.url


def GetAndPrintFeedByUrl():
  yt_service = gdata.youtube.service.YouTubeService()

  # You can retrieve a YouTubeVideoFeed by passing in the URI
  uri = 'http://gdata.youtube.com/feeds/api/standardfeeds/JP/most_popular'
  PrintVideoFeed(yt_service.GetYouTubeVideoFeed(uri))

def SearchAndPrint(search_terms):
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.vq = search_terms
  query.time = 'today'
  query.orderby = 'viewCount'
  query.racy = 'include'
  feed = yt_service.YouTubeQuery(query)
  PrintVideoFeed(feed)


def GetAndPrintUserUploads(username):
  yt_service = gdata.youtube.service.YouTubeService()
  uri = 'http://gdata.youtube.com/feeds/api/users/%s/uploads' % username
  PrintVideoFeed(yt_service.GetYouTubeVideoFeed(uri))

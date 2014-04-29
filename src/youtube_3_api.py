#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


DEVELOPER_KEY = "AIzaSyDkbupZc60XCCfJmXH39yxyUfOSaQQ03dQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
            developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
          type="video",
          channelId="UCG-KeToSZQ_2PSc2si4FrYw",
          publishedAfter="2014-04-01T00:00:00Z",
          part="snippet",
          order="date",
          maxResults=10,
          ).execute()

    videos = []
    channels = []
    playlists = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
              videos.append("%s (%s)" % (search_result["snippet"]["title"],
                  search_result["id"]["videoId"]))
        elif search_result["id"]["kind"] == "youtube#channel":
            channels.append("%s (%s)" % (search_result["snippet"]["title"],
                search_result["id"]["channelId"]))
        elif search_result["id"]["kind"] == "youtube#playlist":
            playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                search_result["id"]["playlistId"]))

    print "Videos:\n", "\n".join(videos), "\n"
    print "Channels:\n", "\n".join(channels), "\n"
    print "Playlists:\n", "\n".join(playlists), "\n"


if __name__ == "__main__":
    argparser.add_argument("--q", help="Search term", default="MADubstep")
    argparser.add_argument("--max-results", help="Max results", default=25)
    args = argparser.parse_args()

    try:
        youtube_search(args)
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

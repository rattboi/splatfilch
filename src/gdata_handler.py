#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from collections import namedtuple
import textwrap

channel = namedtuple('channel', 'uuid name description')
video = namedtuple('video', 'url title')

class gdata_handler(object):
    DEVELOPER_KEY = "AIzaSyDkbupZc60XCCfJmXH39yxyUfOSaQQ03dQ"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    youtube = None

    def __init__(self):
        self.youtube = build(
            self.YOUTUBE_API_SERVICE_NAME,
            self.YOUTUBE_API_VERSION,
            developerKey=self.DEVELOPER_KEY)

    def find_channel(self, channel_name):
        results = []
        response = self.youtube.search().list(
            type='channel',
            q=channel_name,
            part='id,snippet',
            maxResults=5,
            ).execute()

        for search_result in response.get("items", []):
            if search_result['snippet']['description'] != "":
                results.append(
                    channel(name=search_result['snippet']['title'],
                        uuid=search_result['snippet']['channelId'],
                        description=search_result['snippet']['description'])
            )
        return results


if __name__ == "__main__":
    try:
        h = gdata_handler()
        r = h.find_channel("Monstercat")

        for i in range(len(r)):
            print "%d - %s\n    %s\n" % (i+1, r[i].name, r[i].description)

    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

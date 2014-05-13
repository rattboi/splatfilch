#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from collections import namedtuple
from datetime import datetime, timedelta
from rfc3339 import rfc3339

channel_t = namedtuple('channel', 'id title description')
video_t = namedtuple('video', 'id title')

DEVELOPER_KEY = "AIzaSyDkbupZc60XCCfJmXH39yxyUfOSaQQ03dQ"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube():
    return build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)

def find_channels(channel_name, max_results):
    results = []
    response = youtube().search().list(
        type='channel',
        q=channel_name,
        part='id,snippet',
        maxResults=max_results,
        ).execute()

    for search_result in response.get("items", []):
        if search_result['snippet']['description'] != "":
            results.append(
                channel_t(
                    title=search_result['snippet']['title'],
                    id=search_result['snippet']['channelId'],
                    description=search_result['snippet']['description']
                )
            )
    return results


def find_videos(channel_id, datetime_since, max_results):
    results = []
    response = youtube().search().list(
        type='video',
        channelId=channel_id,
        publishedAfter=rfc3339(datetime_since),
        part='id,snippet',
        maxResults=max_results,
        ).execute()

    for search_result in response.get("items", []):
        if search_result['snippet']['description'] != "":
            results.append(
                video_t(
                    title=search_result['snippet']['title'],
                    id=search_result['id']['videoId']
                )
            )
    return results

if __name__ == "__main__":
    Monstercat = "UCJ6td3C9QlPO9O_J5dF4ZzA"
    now = datetime.now()
    last_week = now - timedelta(days=7)

    for i in find_channels('Monstercat', 5):
        print i.id, i.title

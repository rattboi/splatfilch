#!/usr/bin/env python
import re
from collections import namedtuple

regex_t = namedtuple("Regex_Type", "re artist title")
common = regex_t("^(.+?)( - )(.+?)$", 1, 3)

def title_parse(videoname):
    """ extracts artist(s) and song title from youtube video title

    >>> title_parse("Artist - Title")
    ('Artist', 'Title')

    >>> title_parse("[ignored] Artist - Title")
    ('Artist', 'Title')

    >>> title_parse("[ignored] Artist - Title [ignored]")
    ('Artist', 'Title')

    >>> title_parse("Artist - Title [ignored]")
    ('Artist', 'Title')

    >>> title_parse("Artist - Title (remix) [ignored]")
    ('Artist', 'Title (remix)')

    >>> title_parse("Artist & Artist - Title")
    ('Artist & Artist', 'Title')
"""
    # try the simple case first:
    attempt = re.search(common.re, videoname)
    artist = attempt.group(common.artist)
    title = attempt.group(common.title)

    # remove square bracketed fields from artist, if present
    if ('[' in artist) or ('[' in artist):
        artist = re.sub('\[(.+?)\] ', '', artist)

    # similarly for these fields following the title
    if ('[' in title) or ('[' in title):
        title = re.sub(' \[(.+?)\]', '', title)

    return (artist, title)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


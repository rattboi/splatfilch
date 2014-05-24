#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# pylint: disable=anomalous-backslash-in-string,line-too-long
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

    >>> title_parse("Savant - 8-Bit Lightsaber (Original Mix) [SectionZ Records]")
    ('Savant', '8-Bit Lightsaber (Original Mix)')

    >>> title_parse("[Dubstep] - Au5 - Blossom [Monstercat EP Release]")
    ('Au5', 'Blossom')

    >>> title_parse("*Drumstep* Spag Heddy & Panda Eyes - Nafta")
    ('Spag Heddy & Panda Eyes', 'Nafta')

    >>> title_parse("Electro House: Zentra - Conditions")
    ('Zentra', 'Conditions')

    >>> title_parse("SOULERO - Burning Down (Ft. Meron Ryan) - Kaster Mix")
    ('SOULERO', 'Burning Down (Ft. Meron Ryan) - Kaster Mix')

    >>> title_parse(u"►SubSIL3NT Podcast 081 [Electro/House]")
    ('', 'SubSIL3NT Podcast 081 [Electro/House]')

    >>> title_parse("HD Dubstep | Teminite - Shockwave [Free Download]")
    ('Teminite', 'Shockwave')

    >>> title_parse("[Chillstep]: Twofold - Skyfire ( Avien Remix )")
    ('Twofold', 'Skyfire ( Avien Remix )')

    >>> title_parse("Peking Duk -- High (Yahtzel Remix)")
    ('Peking Duk', 'High (Yahtzel Remix)')
"""
    # remove unicode characters, if present
    videoname = videoname.encode('ascii', 'ignore')

    # before counting dashes, fix a rare (stupid) case where uploaders use
    # 2 dashes instead of 1
    if '--' in videoname:
        videoname = re.sub('--', '-', videoname)

    # number of dashes can help to determine format
    dashes = re.findall(" - ", videoname)

    # it probably isn't a song if there is no dash...
    if len(dashes) == 0:
        return ('', videoname)

    # a rare case where '*text*' appears at the front of the title
    if len(re.findall(r'\*', videoname)) == 2:
        videoname = re.sub(r'\*(.+?)\* ', '', videoname)

    # a rare case where 'text: ' appears at the front of the title
    if ': ' in videoname:
        videoname = re.sub(r'^(.+?): ', '', videoname)

    # a rare case where 'text | ' appears at the front of the title
    if ' | ' in videoname:
        videoname = re.sub(r'^(.+?) \| ', '', videoname)

    # commonly, this means '[text] - artist - title ... '
    # in this case, the leading '[text] -' can be deleted, then
    # parsing can continue using single-dash algorithm
    if len(dashes) == 2:
        videoname = re.sub(r'^\[(.+?)\] - ', '', videoname)

    # single-dash algorithm: split into two fields at the dash,
    # then remove '[text]' from each, if present
    attempt = re.search(common.re, videoname)
    artist = attempt.group(common.artist)
    title = attempt.group(common.title)

    # remove square bracketed fields preceeding artist, if present
    if ']' in artist:
        artist = re.sub('\[(.+?)\] ', '', artist)

    # similarly for these fields following the title
    if '[' in title:
        title = re.sub(' \[(.+?)\]', '', title)

    return (artist, title)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


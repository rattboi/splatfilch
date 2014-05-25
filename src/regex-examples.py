#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# pylint: disable=anomalous-backslash-in-string,line-too-long
import re

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

    # stop processing if there are no dashes, as it probably isn't a song
    if '-' not in videoname:
        return ('', videoname)

    # convert double dashes to single. in this routine, ' - ' ==  ' -- '
    if '--' in videoname:
        videoname = re.sub('--', '-', videoname)

    # number of dashes can help to determine format
    dashes = re.findall(" - ", videoname)

    # a rare case where '*text*' appears at the front of the title
    if len(re.findall(r'\*', videoname)) == 2:
        videoname = re.sub(r'\*(.+?)\* ', '', videoname)

    # a rare case where 'text: ' appears at the front of the title
    if ': ' in videoname:
        videoname = re.sub(r'^(.+?): ', '', videoname)

    # a rare case where 'text | ' appears at the front of the title
    if ' | ' in videoname:
        videoname = re.sub(r'^(.+?) \| ', '', videoname)

    # a rare case where '[text] - ' appears at the front of the title
    if len(dashes) == 2 and '[' in videoname:
        videoname = re.sub(r'^\[(.+?)\] - ', '', videoname)

    # single-dash algorithm: split into two fields at the dash,
    # then remove '[text]' from each, if present
    attempt = re.search('^(.+?)( - )(.+?)$', videoname)
    artist = attempt.group(1)
    title = attempt.group(3)

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


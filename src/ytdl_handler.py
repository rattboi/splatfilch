#!/usr/bin/env python
'''the call_youtube_dl function lives here'''

import subprocess

def call_youtube_dl(url, channel, artist, track):
    '''downloads specified url, using channel, artist, and track to
 specify the output name.  returns False indicating no errors, else
 returns True indicating that youtube-dl call produced stderr output'''

    oformat = artist + " - " + track + " [" + channel + "]" + ".%(ext)s"

    proc = subprocess.Popen(['youtube-dl', '-o', oformat, url],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    proc.wait()

    with open("youtubedl.log", "w") as ofile:
        ofile.write(stderr+stdout)

    return False if len(stderr) == 0 else True

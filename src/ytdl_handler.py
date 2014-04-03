#!/usr/bin/env python

import subprocess

def download_convert(url, channel, artist, track):
    log_filename = "./ytdl.log"
    output_format = artist + " - " + track + \
        " [" + channel + "]" + '''.%(ext)s'''
    with open(log_filename, "w") as f:
        subprocess.call(['youtube-dl', '-o', output_format, url], stdout=f)
    return

download_convert('''https://www.youtube.com/watch?v=EfvIy236mR8''',
        "mychannel", "myartist", "mysong")

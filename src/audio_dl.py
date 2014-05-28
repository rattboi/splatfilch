#!/usr/bin/env python
''' wrapper around youtube-dl to simplifying audio downloading.  also downloads
the video thumbnail, and allows manual specification of artist and track name
'''

import subprocess
import logging

def download(video_id, artist, title):
    '''downloads specified url, using channel, artist, and track to
 specify the output name.  returns False indicating no errors, else
 returns True indicating that youtube-dl call produced stderr output

 usage:

    # attempt to download a file, this should return errors encountered = false
    >>> download('L9SdtpaEKus', 'Savant', 'Firecloud (Original Mix)')
    False

    # did the file download?
    >>> print os.path.exists('Savant - Firecloud (Original Mix).m4a')
    True

    # did the thumbnail download too?
    >>> print os.path.exists('Savant - Firecloud (Original Mix).jpg')
    True
'''
    logger = logging.getLogger('audio_dl')
    oformat = artist + " - " + title + ".%(ext)s"

    proc = subprocess.Popen(
        ['youtube-dl',                  # run youtube-dl with these options:
            '-q',                       # - quiet, no output unless error
            '-o', oformat,              # - name file '%(artist) - %(song).%ext'
            '--ignore-errors',          # - continue (if possible) on errors
            '--min-filesize', '500k',   # - don't download tiny files
            '--max-filesize', '300m',   # - ... or huge ones
            '--write-thumbnail',        # - download the video thumbnail
            '--format', 'bestaudio',    # - use best audio format
            '--extract-audio',          # - do audio extraction (remove video)
            '--audio-format', 'best',   # - best quality audio format
            '--audio-quality', '0',     # - best quality audio extraction
            video_id],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    # capture output from call to youtube-dl
    stdout = proc.communicate()
    stderr = stdout[0]

    # wait for youtube-dl to terminate
    proc.wait()

    # if errors occurred, log them
    if len(stderr) > 0:
        logger.warning('youtube-dl encountered errors, see the following:\n\n'
            + stderr)
        logger.warning('           [end of youtube-dl errors]')

    else:
        logger.info('youtube-dl call encountered no errors')

    # Errors occurred:  False (no errors) or True (got heem)
    return False if len(stderr) == 0 else True

if __name__ == '__main__':
    import doctest
    import os
    logging.basicConfig(level=logging.DEBUG)
    doctest.testmod()

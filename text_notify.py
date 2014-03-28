!/usr/bin/env python

import smtplib
import json
from pprint import pprint

# Send a text message notifying them of a new song by artist (based on their choices)
# This opens json file containing needed values
# TODO: Investigate IMAP 

def text_notify(artist, song_id):
    json_data=open('privates.json')
    data = json.load(json_data)
    json_data.close()
    message = "New song '%s' by '%s' was uploaded today" % (song_id, artist)
    msg = """From: %s
    To: %s
    Subject: New song by %s
    %s""" % (data['credentials']['username'], data['phonebook']['Erik Rhodes'], artist, message)

    server = smtplib.SMTP('smtp.gmail.com',587)
    #Problem with texts triggering antivirus scan: 'X-Antivirus: avast!... '
    #Could strip and reforward?
     
    try:
        server.starttls()
        server.login(data['credentials']['username'],data['credentials']['password'])
        server.sendmail(data['credentials']['username'], data['phonebook']['Erik Rhodes'], message)
    except:
        print "Could not send email"
    finally:
        server.quit()

#!/usr/bin/env python

import smtplib
# Send a text message notifying them of a new song by artist (based on their choices)
# Has not been tested
# Needs to pass person, artist, and song info as args

import privates
     
#Currently the providers aren't being used
service_providers =
         {
             "Rogers" :   "pcs.rogers.com",
             "Sprint" :   "messaging.sprintpcs.com",
             "tMobile":   "tmomail.net",
             "Telus"  :   "msg.telus.com",
             "Verizon":   "vtext.com",
             "ATT"    :   "mms.att.net"
         }

message = "New song %s by %s was released today" % (song_id, artist)
msg = """From: %s
To: %s
Subject: New song by %s
%s""" % (username, phonebook[person], artist, message)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(username,password)
server.sendmail(username, phonebook[person], msg)
server.quit()
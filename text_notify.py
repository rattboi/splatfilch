!/usr/bin/env python

import smtplib
import json
from pprint import pprint

# Send a text message notifying them of a new song by artist (based on their choices)
# This opens json file containing needed values
# TODO: Correctly construct email message, investigate IMAP 

def main():
    '''In the future, this could read the correct user from a file and depending and select the
    correct message to send as well'''
    message = "Hey, how's it going? Got Heem!"
    subject = "Unimportant information"
    person  = "Erik Rhodes"
    full_message = make_email_message(person, subject, message)
    send_message(person, full_message, 'email')

def make_new_song_text(artist, song_id):
    '''Creates the message based off the artist and song_id, which are pulled from youtube-dl.'''
    return "New song '%s' by '%s' was uploaded today" % (song_id, artist)

def make_email_message(person, subject, message):
    ''' Constructs email from given information (generic method).  Pass string of person's name.''' 
    json_data=open('privates.json')
    data = json.load(json_data)
    json_data.close()
    message = """From: %s
    To: %s %s
    Subject: %s
    %s""" % (data['credentials']['username'],person, data['phonebook'][person][1], subject, message)
    # Need to use message builder, http://docs.python.org/2/library/email.parser.html#email.message_from_string.
     
    return message

def send_message(person, message, service):
    '''Sends message to any person in our phonebook. Service selects which technology is used
    (text or email). '''
    # open phonebook info
    json_data=open('privates.json')
    data = json.load(json_data)
    json_data.close()
    server = smtplib.SMTP('smtp.gmail.com',587)

    #select correct list index to get correct email or text address
    if service == 'text' or 'Text':
        s = 0
    elif service == 'email' or 'Email':
        s = 1
    else:
        print ("Incorrect service option selected.  Please enter 'text' or 'email'")

    #Problem with texts triggering antivirus scan: 'X-Antivirus: avast!... '
    
    try:
        server.starttls()
        server.login(data['credentials']['username'],data['credentials']['password'])
        server.sendmail(data['credentials']['username'], data['phonebook'][person][s], message)
    except:
        print "Could not send email"
    finally:
        server.quit()

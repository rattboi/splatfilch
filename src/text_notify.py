!/usr/bin/env python

import smtplib
import json
from pprint import pprint
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    full_msg = MIMEMultipart('alternative')
    # plaintext version of message
    full_msg['Subject'] = '%s' %subject
    full_msg['From']    = '%s' % data['credentials']['username']
    full_msg['To']      = '%s' % data['phonebook'][person][1]
    text = "%s" % message 
   
    # html version of message
    html = """\
    <html>
        <head></head>
        <body>
            <p> This is the HTML Version of the message <br>
            This should be sent as an argument in the future. 
            </p>
        </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    full_msg.attach(part1)
    full_msg.attach(part2)
    return full_msg.as_string()

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

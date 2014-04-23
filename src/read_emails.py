import imaplib

def read_emails():
    serv = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    json_data=open('privates.json')
    data = json.load(json_data)
    json_data.close()
    serv.login(data['credentials']['username'], data['credentials']['password'])

    serv.select('INBOX')
    status, response = serv.status('INBOX', "(UNSEEN)")
    unreadcount = int(response[0].split()[2].strip(').,]'))
    # if there are any unread emails
    if unreadcount:
       # check the subject and parse data inside
       # write it to the privates.json file
       # send confirmation email/text of subscription



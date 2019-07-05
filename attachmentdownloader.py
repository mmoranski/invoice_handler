# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:41:04 2019

@author: Moranski
"""


import getpass
import imaplib
import os
import email


# Email account invoices sent to. Can Be changed to getpass.getpass('Email Account: ') 
EMAIL_ACCOUNT = 'invoiceprocessdump@gmail.com'


M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login(EMAIL_ACCOUNT, getpass.getpass('Password: '))
M.select('Inbox')
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)' )
    raw_email = data[0][1]

# converts byte literal to string removing b''

    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

    for part in email_message.walk():
   
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join('/Documents/New DB Project', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
            subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
            print('Downloaded "{file}" from email titled "{subject}"'.format(file=fileName, subject=subject, ))
             
M.close()
M.logout()

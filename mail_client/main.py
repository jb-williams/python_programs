#!/usr/bin/env python3
## email client tutorial on freecode.com done by neuralNine

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
                    # smtp.google is an example change to your email's smtp
server = smtplib.SMTP('smtp.google', 25)

# call the start of there service(start the whole process
server.ehlo()

# Best practice is to put password in an encrypted txt file
# load that file, then decrypt it and use that password
# this one will be example hardcoded as a proof of concept easily changed
#sever.login('mail@mail.com', 'password123')

# loads a non encrypted password file
with open('password.txt', 'r') as f:
    password = f.read()

server.login('testmail@email.com', password)

msg = MIMEMultipart()
msg['From'] = 'jb'
msg['To'] = 'mailtest@email.com'
msg['Subject'] = 'Just a test'

with open('message.txt', 'r') as f:
    message = f.read()

# attach message
msg.attach(MIMEText(message, 'plain'))

# attach attachments, like pictures
filename = '/path/to/pic.jpg' # path relative if in current dir absolute if somewhere else
attachment = open(filename, 'rb')

# payload objec
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Dispostion', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('testmail@email.com', 'mailtest@email.com', text)

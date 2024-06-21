#!/usr/bin/env python3

#use the email.message.EmailMessage class to create an empty email message.
from email.message import EmailMessage
message = EmailMessage()
#print(message)

#add the sender and recipient to the message
sender = "me@example.com"
recipient = "you@example.com"

#add them to the From and To fields of the message
message['From'] = sender
message['To'] = recipient
print(message)

#Add the subject
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
print(message)
#output:Subject: Greetings from me@example.com to you@example.com!

#add a message body
body = """Hey there!

I'm learning to send emails using Python!"""
message.set_content(body)

print(message)

#Adding Attachments

#use the Python mimetypes module to know tell them what sort of file you’re sending.
import os.path
attachment_path = "/Users/macbook/Downloads/IMG_0493-Photoroom.png"
attachment_filename = os.path.basename(attachment_path)

import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)

#output:image/png
#mime_type string contains the MIME type and subtype

#let's split them
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
#output:image
print(mime_subtype)
#output:png

#add the attachment to our message
with open(attachment_path, 'rb') as ap:
     message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))

print(message)


### Sending an email through an SMTP server
# we’ll send the message using the built-in smtplib Python module

import smtplib

#Let's create a smtplib.SMTP object(represent mail server and try to connect to the local machine
mail_server = smtplib.SMTP('localhost')

#output:This error means that there's no local SMTP server configured
#The SMTP class will make a direct SMTP connection, and the
#SMTP_SSL class will make a SMTP connection over SSL/TLS.
mail_server = smtplib.SMTP_SSL('smtp.example.com')

#set the debug level on the SMTP or SMTP_SSL object to see msgs sent by smtplib module
mail_server.set_debuglevel(1)

# authenticate to the SMTP server
import getpass
mail_pass = getpass.getpass('Password? ')

print(mail_pass)

#now we can login
mail_server.login(sender, mail_pass)

#Sending your message
mail_server.send_message(message)
#The send_message method returns a dictionary of any recipients that weren’t able to receive the message

#close the connection to the mail server.
mail_server.quit()

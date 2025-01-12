from email import message
import smtplib

import config

smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'xxx@hotmail.com'
to_email = 'arata.takenouchi.1230@gmail.com'
username = 'arata.takenouchi.1230@gmail.com'
password = '97246242a1'

msg = message.EmailMessage()
msg.set_content('Test email')
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()

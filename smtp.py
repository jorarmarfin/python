# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
message = "Test de envio de emails 3"
 
# setup the parameters of the message
# server = smtplib.SMTP('mail.smtp2go.com')
# user = "developer@gmail.com"
# password = "YzBpZHJwZ2k1c2Yw"
server = smtplib.SMTP('mailserver.ins.gob.pe')
user = "repositorio@ins.gob.pe"
password = "R3p0s1t0r102i19"

msg['From'] = "luis.mayta@gmail.com"
msg['To'] = "luis.mayta@drinux.com"
msg['Subject'] = "Subscription"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
 
server.starttls()

# Login Credentials for sending the mail
server.login(user, password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print("successfully sent email to %s:" % (msg['To'])) 
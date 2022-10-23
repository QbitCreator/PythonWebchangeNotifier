import ssl
import json
import time
import requests
import smtplib
from email.message import EmailMessage

email_id="YourSenderMail@mail.example"
password="YourSenderMailPassword"
send_to_mail="YourReceiverMail@mail.example"

msg1 = EmailMessage()
msg1['From'] = email_id
msg1['To'] = send_to_mail
msg1.set_content('The Huben K1 is finally available on GoGun!!!')
msg1['Subject'] = 'Huben K1 is finally available on GoGun!!!'

msg2 = EmailMessage()
msg2['From'] = email_id
msg2['To'] = send_to_mail
msg2.set_content('The Huben K1 is finally available on Benke-Sport!!!')
msg2['Subject'] = 'Huben K1 is finally available on Benke-Sport!!!'

msg3 = EmailMessage()
msg3['From'] = email_id
msg3['To'] = send_to_mail
msg3.set_content('In checking availability of Huben K1: Failing to connect to server...')
msg3['Subject'] = 'Connection or Data extraction failure'

msg4 = EmailMessage()
msg4['From'] = email_id
msg4['To'] = send_to_mail
msg4.set_content('Good News... I am still checking the availability of your product!')
msg4['Subject'] = 'Still up and running...'

timer=0

server=smtplib.SMTP("mail.server.example",587)
server.starttls()
server.login(email_id, password)
server.sendmail(email_id, send_to_mail, msg4.as_string())
server.close()

while True:
  server=smtplib.SMTP("mail.gmx.net",587)
  server.starttls()
  server.login(email_id, password)
  
  try:
    gogun = requests.get('https://gogun.de/Huben-K1-Bundle/1000724').text
    benke = requests.get('https://www.benke-sport.de/luftgewehr-huben-k1-selbstlader-lg-5-5mm-7-5j-f-semiautomatik-36727').text
    
    if not "Zur Zeit nicht verfügbar" in gogun:
      server.sendmail(email_id, send_to_mail, msg1.as_string())
    time.sleep(5)
    
    if not "Dieser Artikel steht derzeit nicht zur Verfügung!" in benke:
      server.sendmail(email_id, send_to_mail, msg2.as_string())    
    
  except:
    server.sendmail(email_id, send_to_mail, msg3.as_string())
    
  timer+=1
  time.sleep(5)
  
  if timer==48:
    server.sendmail(email_id, send_to_mail, msg4.as_string())
    timer=0
  server.close()
  time.sleep(1800)
  
    

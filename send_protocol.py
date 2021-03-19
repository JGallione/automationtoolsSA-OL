import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_msg(sender, sender_pass, recipient, subject, message):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    try:
        print('sending mail to ' + recipient + ' about ' + subject)
        mailServer = smtplib.SMTP('smtp-mail.outlook.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(sender, sender_pass)
        mailServer.sendmail(sender, recipient, msg.as_string())
        mailServer.close()
    except Exception as e:
        print(str(e))

def send_text(recipient, subject, message):
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    try:
        print('sending mail to ' + recipient + 'on' + subject)
        mailServer = smtplib.SMTP(smtp-mail.outlook.com, 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.send_mail(username, recipient, msg.as_string())
        mail.Server.close()
    except error as e:
        print(str(e))


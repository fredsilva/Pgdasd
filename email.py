# encoding: utf-8

import smtplib
import time
from email.mime.text import MIMEText
#from email.mime.text import MIMEText

import os

# authentication
gmail_user = 'fredsilva.sistemas@gmail.com'
gmail_pwd = 'if(login==true)'

recipient = "frederico@sefaz.to.gov.br"
preable = """A
multiline
message.
"""
end_message = "\n\nRegards,\nΔημήτρης"


def mail(to, subject, text):
    msg = MIMEText(text.encode('utf-8'), 'plain', 'UTF-8')

    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject.encode('utf-8')
    msg.set_charset('utf-8')

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()


def get_quote():
    """ Generate a random message from a fortune collection. """
    f = os.popen("fortune /home/myle/myle-quotes")
    b = f.read()

    return b


def send_specific_message(counter, quote):
    """ Send a message with a specific structure. """
    topic = "A message (" + str(counter) + ')'
    message = preable + quote + end_message
    mail(recipient,
        topic,
        message)


def main():
    i = 0
    while True:
        i += 1
        quote = get_quote()
        send_specific_message(i, quote)
        time.sleep(60 * 60)


if __name__ == '__main__':
    main()
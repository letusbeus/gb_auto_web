import datetime
import os
import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_report(from_address, to_address, mail_password, report_name):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_log'

    with open(report_name, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(report_name))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(report_name)
        msg.attach(part)

    body = 'Logfile is attached.'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(from_address, mail_password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()

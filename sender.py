import datetime
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
import yaml

with open('testdata.yaml') as t:
    testdata = yaml.safe_load(t)

html_report_name = testdata['html_report']
pytest_html_report_name = testdata['pytest_html_report']
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def send_report():
    msg = MIMEMultipart()
    msg['From'] = testdata['mail_address']
    msg['To'] = testdata['mail_address']
    msg['Subject'] = f'{timestamp}_test_report'

    with open(html_report_name, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(html_report_name))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(html_report_name)
        msg.attach(part)

    with open(pytest_html_report_name, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(pytest_html_report_name))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(pytest_html_report_name)
        msg.attach(part)

    body = 'All tests completed.'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(testdata['mail_address'], testdata['mail_password'])
    text = msg.as_string()
    server.sendmail(testdata['mail_address'], testdata['mail_address'], text)
    server.quit()

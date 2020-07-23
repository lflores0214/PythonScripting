import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = ''
email['to'] = ''
email['subject'] = "There are sexy singles in your area"

email.set_content(html.substitute({"name": "Fry"}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('johndoesit92@gmail.com', 'C3darW00d30')
    smtp.send_message(email)
    print('all good!')

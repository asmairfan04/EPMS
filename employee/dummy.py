from re import sub
import static
import random
import qrcode
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd


x=random.randint(10000000,99999999)
im=qrcode.make("OTP is "+str(x))
t=str(6)
im.save(r"employee/static/qr/"+t+".jpg")
path="employee/static/qr/"+t+".jpg"




import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
### Add new subclass for adding attachments
##############################################################
from email.mime.application import MIMEApplication
##############################################################
## The pandas library is only for generating the current date, which is not necessary for sending emails
import pandas as pd

# Define the HTML document
html = '''
    <html>
        <body>
            <h1>Scan the QR code</h1>
            <p>Enter the 8-digit OTP generated!</p>
        </body>
    </html>
    '''

# Define a function to attach files as MIMEApplication to the email
##############################################################
def attach_file_to_email(email_message, filename):
    # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    # Add header/name to the attachments    
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Attach the file to the message
    email_message.attach(file_attachment)
##############################################################    

# Set up the email addresses and password. Please replace below with your email address and password
email_from = 'epms.major@gmail.com'
password = 'beqcpwbqikkegvtu'
email_to = 'arisha.asma@gmail.com'

# Generate today's date to be included in the email Subject
date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'EPMS Validation - {date_str}'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))

# Attach more (documents)
##############################################################
attach_file_to_email(email_message, path)
##############################################################
# Convert it as a string
email_string = email_message.as_string()

# Connect to the Gmail SMTP server and Send Email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_from, password)
    server.sendmail(email_from, email_to, email_string)
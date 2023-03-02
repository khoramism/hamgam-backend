from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
Password = 'Ham*Cos^di'
FROM_EMAIL = 'alireza@ham-ghadam.ir'
FROM_NAME = 'ALirexza'
TO_NAME = 'ghol bolbol'
SUBJECT = f'BADbiodyacjsapcj'
HTML_TEMPLATE = '/home/mehdi/source/Back/hamgam-backend/hamgam/hamgam_backend/email.html'
def send_email():
    sender = FROM_EMAIL
    receiver = ["momom58856@zfobo.com", 'khoramism@gmail.com', 'alirezakhoramimn@gmail.com', 'hamghadam.ir@gmail.com', 'elmamot.abo@gmail.com','elmamot.abo1@gmail.com'] # emails in list for multiple or just a string for single.
    msg = MIMEMultipart()
    msg['From'] = FROM_NAME # The name the email is from e.g. Adam
    msg['To'] = TO_NAME # The receivers name
    msg['Subject'] = SUBJECT
    with open(HTML_TEMPLATE) as f:
        html = f.read()
    part = MIMEText(html, 'html')
    msg.attach(part)

    with smtplib.SMTP('mail.ham-ghadam.ir', 587) as connection:
        #connection.starttls()
        connection.starttls() 
        connection.ehlo()
        connection.login(FROM_EMAIL,  Password)
        connection.sendmail(sender, receiver, msg.as_string())# Import smtplib for the actual sending function
        connection.quit()
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
#with open(textfile) as fp:
##    # Create a text/plain message
#msg = EmailMessage()
#msg.set_content('kir hasckacka[s')
#
## me == the sender's email address
## you == the recipient's email address
#msg['Subject'] = 
#msg['From'] = 
#msg['To'] = 'momom58856@zfobo.com'
#
## Send the message via our own SMTP server.
#s = smtplib.SMTP('mail.ham-ghadam.ir')
#s.send_message(msg)
#s.quit()
send_email()
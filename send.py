import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create a MIMEText object to represent the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body of the email to the message
    msg.attach(MIMEText(body, 'plain'))

    # Start the SMTP session
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Close the SMTP session
    server.quit()

# Example usage
sender_email = SENDER_EMAIL
sender_password = SENDER_PASSWORD
receiver_email = RECEIVER_EMAIL
subject = "Approval Request | PLEASE REPLY"
body = "A new server is requesting approval. Provisioning will not begin until approved. Please reply to this email with Approve to approve, or Deny to deny."

send_email(sender_email, sender_password, receiver_email, subject, body)

# ref: https://medium.com/@thakuravnish2313/sending-emails-with-python-using-the-smtplib-library-e5db3a8ce69a
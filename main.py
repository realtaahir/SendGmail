import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_gmail(sender_email, sender_password, recipient_email, subject, message):
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server for Gmail
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        # Start TLS for security
        server.starttls()

        # Login to your Gmail account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

    print("Email sent successfully!")

# Replace these variables with your actual Gmail credentials and recipient email
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'
recipient_email = 'recipient_email@gmail.com'
subject = 'Test Email'
message = 'This is a test email sent from Python.'

# Call the function to send the email
send_gmail(sender_email, sender_password, recipient_email, subject, message)

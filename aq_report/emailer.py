import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FROM_EMAIL = "x@x.x"
TO_EMAIL = "y@y.y"
SUBJECT = "AirQuality"

def send_email(html_body):
    msg = MIMEMultipart('alternative')
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(html_body, 'html'))

    try:
        with smtplib.SMTP('localhost') as server:  # Change to your SMTP if needed
            server.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

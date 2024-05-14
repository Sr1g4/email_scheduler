import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
password = os.getenv("EMAIL_PASSWORD")

print(f"Sender Email: {sender_email}")
print(f"Receiver Email: {receiver_email}")
print(f"Password: {password if password else 'No Password Retrieved'}")


subject = "Daily Reminders"
body = """
This is an automated email sent by my email scheduler.

Hello Sri,

Dont Forget:
- Wake up early at a consistent time.
- Practice a short meditation or mindfulness exercise.
- Engage in physical exercise (like a brief walk, yoga, or a gym session).
- Have a healthy breakfast.
- Review what you have to do today: canvas API should get installed soon.
- Take some breaks.
- DON'T STRESS, LIFE GOES ON!!!!!
Daily Tasks:
    Apply for internships 
    Do Canvas Homework
    Call your Parents
"""

# Send email function
def send_email():
    message = MIMEMultipart()
    message["From"] = 'Sri Gadicherla'
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")

while True:
    send_email()
    time.sleep(3600)
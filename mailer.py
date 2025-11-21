import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

def send_email(report, recipient):
    """
    Sends the analysis report via email.
    
    Args:
        report (str): The analysis report text.
        recipient (str): The email address of the recipient.
    """
    if not config.EMAIL_SENDER or not config.EMAIL_PASSWORD:
        print("Email credentials missing. Skipping email.")
        return

    msg = MIMEMultipart()
    msg['From'] = config.EMAIL_SENDER
    msg['To'] = recipient
    msg['Subject'] = "Stock Analysis Report"

    msg.attach(MIMEText(report, 'plain'))

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(config.EMAIL_SENDER, config.EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(config.EMAIL_SENDER, recipient, text)
        server.quit()
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Test run
    send_email("This is a test report.", config.EMAIL_SENDER)

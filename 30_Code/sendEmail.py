import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(
        receiver_email="rohitianaditya@gmail.com",
        subject="Image Share 2",
        body="Upload the share of the Image into application",
        image_file=None):
    
    # Email credentials and details
    sender_email = "vasteadi45@gmail.com"
    password = "eanb ndxf ryqv xrwi"

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # Attach the image if provided
    if image_file:
        with open(image_file, 'rb') as fp:
            img_data = fp.read()
            # img_data = image_file
            image = MIMEImage(img_data, name="image.jpg")
            message.attach(image)

    # Create SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace 'smtp.example.com' with your SMTP server address and port
    try:
        server.starttls()  # Enable TLS
        server.login(sender_email, password)  # Login

        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the SMTP server
        server.quit()

# Example usage:
# send_email(receiver_email="rohitianaditya@gmail.com", subject="Test Email", body="Hello!", image_file="v1.jpg")

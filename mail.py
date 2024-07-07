import os
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail:
    def __init__(self, sender_email, host: str="smtp.gmail.com", port: int= 587):
        self.sender_email = sender_email
        self.host = host
        self.port = port
        self.mail_password = os.environ.get('mail_app_pswd')


    def send_email_using_emailmessage(self, to_email, subject, body):
        try:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] =self.sender_email
            msg["To"] = to_email
            msg.set_content(body)

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.sender_email, self.mail_password)
                server.send_message(msg)
                print("mail sent successfully")
        except Exception as e:
            print(f"Exception has occured while sending email to {to_email}. Error {e}")

    def send_email_using_mime(self, to_email, subject, html_data=None):
        try:
            msg = MIMEMultipart('alternative')
            msg["Subject"] = subject
            msg["From"] = self.sender_email
            msg["To"] = to_email

            if not html_data:
                with open("mail_template.html", "r") as f:
                    html_data = f.read()

            mime_mail = MIMEText(html_data, "html")
            msg.attach(mime_mail)


            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.sender_email, self.mail_password)
                server.sendmail(self.sender_email, to_email, msg.as_string())
                print("mail sent successfully")
        except Exception as e:
            print(f"Exception has occured while sending email to {to_email}. Error {e}")

# my_email = "radulescu.diana95@gmail.com"
#
# message = "Aici este primul nostru mail"
#

# 1
# server =smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
#
#
# server.login(my_email, "usij jary oxgq wfhx")
#
# server.sendmail(my_email, my_email, message)
#
# server.quit()
#
#
#
# 2
# with smtplib.SMTP("smtp.gmail.com", 587) as server:
#     server.starttls()
#     server.login(my_email, "usij jary oxgq wfhx")
#     server.sendmail(my_email, my_email, message)
#     print("mai sent successfully")

if __name__ == '__main__':
    new_email = Mail("radulescu.diana95@gmail.com")
    # new_email.send_email_using_emailmessage("denisa.r95@gmail.com", "Acesta e subiectul", "Acesta e mesajul")
    new_email.send_email_using_mime("radulescu.diana95@gmail.com", "Acesta e subiectul")

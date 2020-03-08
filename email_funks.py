import smtplib
from email.message import EmailMessage

def send_email(username, password, email_to, title, message):

	email = EmailMessage()
	
	email["from"] = username
	email["to"] = email_to
	email["subject"] = title
	
	email.set_content(message)

	with smtplib.SMTP(host="smtp.mail.com", port=587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login(username, password)
		smtp.send_message(email)
		print("Mail sent...")


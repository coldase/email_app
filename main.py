from email_funks import send_email
from random_funks import clear
from getpass import getpass

clear()
print("Welcome to Email_App 1.0\n")
ask_username = input("Username: ")
ask_password = getpass("Password: ")
if ask_username:
	clear()
	ask_todo = input("Choose\n\n1: Send Email\n2: Quit\n-> ")
	if ask_todo == "1":
		clear()
		ask_email_to = input("Email to: ")
		clear()
		ask_title = input("Title: ")
		clear()
		ask_message = input("Message: ")
		clear()
		print(f"Address: {ask_email_to}")
		print(f"Title: {ask_title}")
		print(f"Message: {ask_message}")
		ask_if_okey = input("Wanna send? y/n\n-> ")
		if ask_if_okey == "y":
			clear()
			send_email(ask_username, ask_password, ask_email_to, ask_title, ask_message)
		else:
			print("Quitting...")
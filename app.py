# Author: Snehashish Laskar
# Date: 29-06-2021
# Github: https://github.com/snehashish090
# Conttact: snehashish.laskar@gmail.com

# Importing the necessary modules
import smtplib, ssl
from timeit import default_timer as timer 

# Authentication
def main():

	# Displaying the notice to enable less secure apps
	print("""
	please enable google less secure apps in your google account
	because in order for this spammer to work, the google account should
	not block the emails you can enable less secure apps at
	https://myaccount.google.com/lesssecureapps
		""")

	# getting the number of emails to be spammed
	number_of_times = int(input("enter the number of emails to be sent: "))

	# Making a default context
	context = ssl.create_default_context()
	# Defining the port for contacting the gmail server
	port = 465

	# Connecting to the gmail server as server
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:

		# Authenticating the user
		username = input("enter your email id: \n")
		password = input("enter password to authenticate: \n")

		# trying to login using the credentials
		try:
			server.login(username, password)
		# If failed then displaying the message to the user
		except:
			print("Either less secure apps is diabled or password or email id is incorrect: \n")
			exit()

		# Getting the reciever and message the user wants to say in the email
		reciever = input("enter the target email adress: \n")
		message = input("enter the message you wanna send: \n")
		
		# Running a for loop for the number of times 
		# the user wants in  the variable number_of_times
		for i in range(number_of_times):
			# Sending the email
			server.sendmail(username, reciever, message)
			# Printing how many times the email has been sent
			print("Done {} time".format(i+1))
main()

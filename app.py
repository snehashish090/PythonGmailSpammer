# Author: Snehashish Laskar
# Date: 29-06-2021
# Github: https://github.com/snehashish090
# Conttact: snehashish.laskar@gmail.com

# Copyright 2022 Snehashish
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


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

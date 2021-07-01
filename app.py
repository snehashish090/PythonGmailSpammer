# Author: Snehashish Laskar
# Date: 29-06-2021
# Github: https://github.com/snehashish090
# Conttact: snehashish.laskar@gmail.com

# Importing the necessary modules
import smtplib, ssl

# Authentication
def main():
	print("""
	please enable google less secure apps in your google account
	because in order for this spammer to work, the google account should
	not block the emails you can enable less secure apps at
	https://myaccount.google.com/lesssecureapps
		""")
	number_of_times = int(input("enter the number of emails to be sent: "))
	context = ssl.create_default_context()
	port = 465

	with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
		username = input("enter your email id: \n")
		password = input("enter password to authenticate: \n")
		try:
			server.login(username, password)
		except:
			print("Either less secure apps is diabled or password or email id is incorrect: \n")
			exit()

		reciever = input("enter the target email adress: \n")
		message = input("enter the message you wanna send: \n")
		for i in range(number_of_times):
			server.sendmail(username, reciever, message)
			print("Done {} time".format(i))
main()







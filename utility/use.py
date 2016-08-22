#this package will include all the necessary functions for the website

from email.mime.text import MIMEText
import smtplib

def sendEmail(receivers, content = "", subject = ""):
	sender = 'zhangchiyuan2@gmail.com'
	message = """
	Subject: SMTP e-mail test

	This is a test e-mail message.
	"""
	password = "jiangshihui2"

	# Open a plain text file for reading.  For this example, assume that
	# the text file contains only ASCII characters.
	txt = "hi, there, \n thanks for your email \n #subject# \n #content#"
	# print txt
	txt = txt.replace("#subject#", subject)
	txt = txt.replace("#content#", content)
	# Create a text/plain message
	msg = MIMEText(txt)
	# print msg
	# print msg

	# me == the sender's email address
	# you == the recipient's email address
	msg['Subject'] = 'Subject'
	msg['From'] = sender
	msg['To'] = receivers

	# print msg

	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	try:
		s = smtplib.SMTP('smtp.gmail.com',587)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(sender,password)
		s.sendmail(sender, receivers, msg.as_string())
	except as e:
		print str(e)
	s.quit()

sendEmail("zhangchiyuan2@gmail.com")
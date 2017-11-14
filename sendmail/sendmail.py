import smtplib
from email.mime.text import MIMEText

#sender, [recipientsList], htmlmsg, subject, serverIP
def sendmail(**kwargs):
	try:
		sender=recipientlist=htmlmsg=subject=serverIP=None
		if kwargs is not None:
			for k,v in kwargs.iteritems():
				if k=='sender' : sender=kwargs[k]
				if k=='recipientlist' : recipientlist=kwargs[k]
				if k=='htmlmsg' : htmlmsg=kwargs[k]
				if k=='subject' : subject=kwargs[k]
				if k=='serverIP' : serverIP=kwargs[k]
		body = htmlmsg
		msg = MIMEText(body, 'html')
		msg['Subject'] = subject
		msg['From'] = sender
		msg['To'] = ", ".join(recipientlist)
		
		#sending
		session = smtplib.SMTP(serverIP)
		session.ehlo()
		session.starttls()
		session.ehlo
		print 'Sending to recipients:-'
		print recipientlist
		send_it = session.sendmail(sender, recipientlist, msg.as_string())
		session.quit()
	except e:
		print 'Exception {0}'.format(str(e))
		raw_input()
		exit()
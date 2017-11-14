import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#sender, [recipientsList], htmlmsg, subject, serverIP, attachment 
def sendmail(**kwargs):
	try:
		HasImg=False
		sender=recipientlist=htmlmsg=subject=serverIP=None
		if kwargs is not None:
			for k,v in kwargs.iteritems():
				if k=='sender' : sender=kwargs[k]
				if k=='recipientlist' : recipientlist=kwargs[k]
				if k=='htmlmsg' : htmlmsg=kwargs[k]
				if k=='subject' : subject=kwargs[k]
				if k=='serverIP' : serverIP=kwargs[k]
				if k=='attachment':
					attachment=kwargs[k]
					HasImg=True
		
			if HasImg == True:
				msg = MIMEMultipart()
				msg['To'] = ", ".join(recipientlist)
				msg["From"] = sender
				msg["Subject"] = subject

				msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % (htmlmsg, attachment), 'html')  
				msg.attach(msgText)   # Added, and edited the previous line

				fp = open(attachment, 'rb')                                                    
				img = MIMEImage(fp.read())
				fp.close()
				img.add_header('Content-ID', '<{}>'.format(attachment))
				msg.attach(img)
			
			else:
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
			
	except Exception, e:
		print 'Exception {0}'.format(str(e))
		raw_input()
		exit()
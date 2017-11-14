from sendmail import sendmail
sendmail.sendmail(sender='pjayaraj@amd.com',
		recipientlist=['pranoy.jayaraj@amd.com'],
		htmlmsg='TestMessage', subject='Test',
		serverIP='10.180.168.6')

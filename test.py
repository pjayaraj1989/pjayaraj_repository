from sendmail import sendmail
from listfunctions import listfunctions

#sendmail.sendmail(sender='pjayaraj@amd.com',recipientlist=['pranoy.jayaraj@amd.com'],htmlmsg='TestMessage', subject='Test',	serverIP='10.180.168.6')
#print listfunctions.GetMaxMin([1,2,3,4,5])
#print listfunctions.SortList(ord='dec',list=[0,0,-1,1,2,3])
print listfunctions.CreateHTMLTable(list=['Pranoy','Jayaraj','28'], header=['First','Last','Age'])

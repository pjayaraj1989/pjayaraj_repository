import os
import subprocess
import sys
import shutil
from email.mime.text import MIMEText
import smtplib
import requests
import random

ScriptPath = os.path.dirname(os.path.abspath( __file__ ))

#global vars
op=[]	

#send mail -- > EDIT
#sender, [recipientsList], htmlmsg, subject, serverIP
def SendMail(**kwargs):
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

#read bin contents
def ReadBinaryFile (File):
  if (os.path.exists(File) == False):
    print "\nError :", File, " does not exist"
    return (None)

  try:
    f = open (File,'rb')
  except:
    Error_Exit('File not found: {0}'.format(File) )
    
  lines = f.read()
  f.close()
  return lines

#substring
def find_between(s, first, last):
	try:
		start = s.index(first) + len(first)
		end = s.index(last, start)
		return s[start:end]
	except ValueError:
		return ''

#copy
def copyFile2(src, dest):
    try:
		shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:		
		print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:		
		print('Error: %s' % e.strerror)

#log into text file
def Log(file,msg):
	f=open(file,'w+')
	f.write(msg)
	f.write('\n')
	f.close()

#execute
def execute(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Poll process for new output until finished
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() is not None:
            break
        sys.stdout.write(nextline)
        sys.stdout.flush()
	output,err = process.communicate()
	exitCode = process.returncode
	print 'Exit code:-' + str(exitCode)
	
	if (exitCode == 0):
		return output
	else:
		raise ProcessException(command, exitCode, output)
	
	return output,err

#create an html table from a list
def CreateHTMLTable(list, header):
	res=''
	html='<html><head><body>'
	html+='<table border=\"2\" cellpadding=\'5\' cellspacing=\'1\''
	html+='style=\'border: solid 2px green; font-size: small;\'>'
	html+='<tr height=\'1px\' align=\'justify\' valign=\'top\' bgcolor=\'gray\'>'
	#add header
	for h in header:
		html+='<th>{0}</th>'.format(h)
	html+='</tr>'
	#add contents
	for l in list:
		html+='<tr'
		for m in l:
			if 'pass' in l:
				res = 'pass'
			else:
				res='fail'
		
		if res == 'pass':
			html+=' style="background-color:white;">'
			for member in l:
				if 'pass' in member:
					html+='<td><font color="green">{0}</font></td>'.format(member.upper())
				else:
					html+='<td><font color="black">{0}</font></td>'.format(member)
		else:
			html+=' style="background-color:white;">'
			for member in l:
				if 'fail' in member:
					html+='<td><font color="red">{0}</font></td>'.format(member.upper())
				else:
					html+='<td><font color="black">{0}</font></td>'.format(member)
				
		html+='</tr>'	
	html+='</table>'	
	return html

#add elements
def Add(*args):
    op=0
    for a in args:
        op+=int(a)
    return op
        
#get pairs in the list which will output sum
def GetPairsForSum(l, sum):
    output=[]
    temp_list=[]
    sub=[]
    for e in l:
        temp_list = l[l.index(e):]
        for t in temp_list:
            if e + t == 9:
                output.append((e,t))
    return output                        

#get index of a list element (list, element)
def GetIndex(**kwargs):
    if kwargs is not None:
        for k, v in kwargs.iteritems():
            if k=='list':
                list=kwargs[k]
            if k=='element':
                element=kwargs[k]

    for i in range(len(list)):
        if list[i] == element:
            return i    
    
#sort get max min
def GetMaxMin(l):
    max=l[0]
    min=l[0]
    for x in l:
        if x > max:
            max = x
        if x < min:
            min = x
    return max,min
 
#sort (ord, array)
def Sort(**args):
    op=[]
    
    if args is not None:
        for k,v in args.iteritems():
            if k=='ord':
                ord=args[k]
            if k=='array':
                array=args[k]
    
    while(array):
        if ord=='inc':
            min=GetMaxMin(array)[1]
            op.append(min)
            array.remove(min)
        if ord=='dec':
            max=GetMaxMin(array)[0]
            op.append(max)
            array.remove(max)
    return op
    
#read folder recursively
def ReadFolderTree(root,type):
	global op
	print 'Checking for {0} files inside {1}'.format(type,root)
	contents=os.listdir(root)
	if len(contents) > 0:
		for f in contents:
			temp=r'{0}\{1}'.format(root,f)
			if os.path.isfile(temp):
				if temp.endswith(type):
					op.append(temp)
			if os.path.isdir(temp):
				ReadFolderTree(temp, type)
	return op

#gen wkeycodes from https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain
def GenerateCode():
	url = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
	r = requests.get(url)
	print 'Generating code...'
	words_list = r.content.splitlines()
	word1 = random.choice(words_list)
	word1 = word1.title()
	word2 = random.choice(words_list)
	word2 = word2.title()
	number = random.randint(0,100)
	symbol = random.choice(['@','#','$','&','~'])
	pw = word1 + word2 + symbol + str(number)
	return pw
	
#main
def main():       
	input=[1,2,3,6,9,0,8,0,8,1]
    #print GetPairsForSum(input, 9)
    #print GetIndex(list=['zero','one', 'two'], element='one')
    #print GetMaxMin(input)[0]
	#print Sort(ord='inc',array=input)
	#f=r'C:\Users\pjayaraj\Desktop\MyScripts'
	#op = ReadFolderTree(f,'.py')
	#SendMail(sender='pjayaraj@amd.com',recipientlist=['pranoy.jayaraj@amd.com'], htmlmsg='TestMessage', subject='Test', serverIP='10.180.168.6')
	#print CreateHTMLTable([['1','Pranoy','28'],['2','Jayaraj','58']], ['No.', 'Name', 'Age'])
	
	print GenerateCode()
	
if __name__== "__main__":
    main()

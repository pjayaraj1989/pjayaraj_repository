import os
import datetime

#copy file 
def copyfile(src,dest):
	if not os.path.isfile(src):
		print 'File {0} does not exist'.format(src)
		raw_input()
		exit()
	#get file extension
	ext='.' + src.split('.')[-1]
	if src==dest:
		print 'Src and Dest file names are same'
		dest=dest.strip(ext) + '_copy_' + ext		
	with open(src,'rb') as s:
		with open(dest,'wb') as d:
			contents=s.read()
			d.write(contents)
	print 'Copied {0} to {1}'.format(src,dest)
	
#log messages into file
def Log(file,msg):
	#if exist, append, else create new file	
	fh = open(file,'a+')
	fh.write('Log on ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + ':- \n')
	fh.write(msg)
	fh.write('\n')
	fh.close()
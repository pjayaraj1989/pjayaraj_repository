import os
op=[]
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
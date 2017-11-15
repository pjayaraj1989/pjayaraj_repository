
def copyfile(src,dest):
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
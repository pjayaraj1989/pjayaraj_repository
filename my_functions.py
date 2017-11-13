import os

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
	print 'Reading ' + root
	contents=os.listdir(root)
	if len(contents) > 0:
		for f in contents:
			temp=r'{0}\{1}'.format(root,f)
			if os.path.isfile(temp):
				if temp.endswith(type):
					print temp
			if os.path.isdir(temp):
				ReadFolderTree(temp, type)
    
#main
def main():       
	input=[1,2,3,6,9,0,8,0,8,1]
    #print GetPairsForSum(input, 9)
    #print GetIndex(list=['zero','one', 'two'], element='one')
    #print GetMaxMin(input)[0]
	#print Sort(ord='inc',array=input)
	f=r'C:\Test'
	print ReadFolderTree(f,'.txt')
    
if __name__== "__main__":
    main()

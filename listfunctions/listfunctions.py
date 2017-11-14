
#sort get max min from a list
def GetMaxMin(l):
    max=l[0]
    min=l[0]
    for x in l:
        if x > max:
            max = x
        if x < min:
            min = x
    return max,min

#sort (ord, list)
def SortList(**args):
    op=[]
    
    if args is not None:
        for k,v in args.iteritems():
            if k=='ord':
                ord=args[k]
            if k=='list':
                list=args[k]    
    while(list):
        if ord=='inc':
            min=GetMaxMin(list)[1]
            op.append(min)
            list.remove(min)
        if ord=='dec':
            max=GetMaxMin(list)[0]
            op.append(max)
            list.remove(max)
    return op
	
#list to html  args:- list, header
def CreateHTMLTable(**kwargs):
	if kwargs is not None:
		for k,v in kwargs.iteritems():
			if k=='list': list=kwargs[k]
			if k=='header' : header=kwargs[k]
			
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
	

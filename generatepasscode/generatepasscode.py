import requests
import random
import datetime

#gen wkeycodes from https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain
#file=file to log the created passwords
def GenerateCode(file):
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
	#if exist, append, else create new file	
	fh = open(file,'a+')
	fh.write(pw + ' generated on ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
	fh.write('\n')
	fh.close()	
	return pw
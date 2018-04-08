import sys
import mailbox
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

'''
def read_mbox(filename):
	mbox = mailbox.mbox(filename)
	i = 0
	sender_file = open('senders.data', 'w')
	for message in mbox:
		sender = message['from'].split()[-1]
		address = re.sub(r'[<>]', '', sender)
		print >>sender_file, address
	sender_file.close()
'''
class MyMbox:
	def __init__(self, filename):
		self.mbox = mailbox.mbox(filename)
	
	def words(self):
		word_list = []
		i = 0
		for message in self.mbox:
			try:
				if message.is_multipart():
					content = ''.join(part.get_payload(decode = True) for part in message.get_payload())
				else:
					content = message.get_payload(decode = True)
				word_list += re.split('\W+', content)
			except:
				pass
		return word_list
			
mbox_file = sys.argv[1]

m = MyMbox(mbox_file)
f = open(mbox_file+".words.nostopwords.data", 'w')
stop_words = set(stopwords.words('english'))

for word in m.words():
	if word not in stop_words:
		print >>f, word


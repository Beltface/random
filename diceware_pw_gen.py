import requests
import sys
import re
from random import randint

try:
	sys.argv[1]
except:
	print "Command usage:"
	print "\tdiceware_pw_gen.py {[pw length in words]}\n"
	sys.exit(1)


if sys.argv[1].isdigit() != True:
	print "Command usage:"
	print "\tdiceware_pw_gen.py {[pw length in words]}\n"
	print "ERROR: Password length must be an integer\n"
	sys.exit(1)

regex = re.compile('\d{5}\s\S+')

word_list = dict(s.split('\t',1) for s in regex.findall(requests.get("http://world.std.com/~reinhold/diceware.wordlist.asc").text))

num_words = int(sys.argv[1])
word = ""

for i in range(0,num_words):
	num_string = ""
	for x in range(0,5):
		num_string += str(randint(1,6))
	word += word_list[num_string] + " "

print "Your new password is %s" % word

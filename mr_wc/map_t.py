import sys	# used to read data
import re	# regular expression

p = re.compile(r'\w+')
for line in sys.stdin:
	ss = line.strip().split(' ')	# Read string line and remove the white space
	for s in ss:
		if len(p.findall(s)) < 1:
			continue
		s_low = p.findall(s)[0].lower()
		print s_low + '\t' + '1'

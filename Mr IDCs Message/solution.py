"""created by : rjohari23"""

import sys
t = int(raw_input())
while t:
	k = int(raw_input())
	s = raw_input()
	l = len(s)
	ans = []
	for i in range(l):
		ans.append((ord(s[i])-97+k)%26)

	#print ans
	for c in ans:
		print chr(c+97),;sys.stdout.softspace=False
	print ''
	t -= 1
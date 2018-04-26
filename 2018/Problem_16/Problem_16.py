a = raw_input()
num = int(a[::-1])
a = int(a)
testfor = 0
if a > 12:
	for i in range(2, a):
		if a % i == 0:
			testfor = 1
			break
if testfor == 1:
	print str(a) + " is not an emirp number"
	exit()
for i in range(2, num):
	if num % i == 0:
		testfor = 1
		break
if testfor == 1:
	print str(a) + " is not an emirp number"
else:
	print str(a) + " is an emirp number"
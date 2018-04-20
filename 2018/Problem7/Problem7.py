a = []
try:
	while True:
		v = int(raw_input())
		if v != 0:
			a.append(v)
		else:
			break
except ValueError:
	print 0
	exit()
try:
	gpu = a[0]
except IndexError:
	print 0
	exit()
total = 0
a[0] = " "
for i in a:
	if i != " ":
		if i <= gpu:
			total += 1
print total

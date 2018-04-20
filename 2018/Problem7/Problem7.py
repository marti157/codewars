a = []
try:
	while True:
		x = int(raw_input())
		if x != 0:
			a.append(x)
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

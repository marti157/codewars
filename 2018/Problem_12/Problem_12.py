a = []
while True:
	try:
		b = raw_input()
		float(b)
	except:
		break
	a.append(float(b))
if len(a) == 0:
	print 0
	exit()
mitjana = 0
for i in a:
	mitjana += i
mitjana = mitjana / len(a)
total = 0
for i in a:
	if i < mitjana:
		total += 1
print total
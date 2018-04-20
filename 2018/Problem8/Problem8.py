a = raw_input()
v = a.split(" ")
total = float(0)
for i in v:
	try:
		total += float(int(i) * 1.6)
	except ValueError:
		pass
if total >= 622:
	print "Yes"
else:
	print "No"
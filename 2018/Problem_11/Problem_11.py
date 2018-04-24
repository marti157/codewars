a = raw_input()
res = [0, 0, 0]
for i in a:
	if i != " ":
		if i.upper() != i:
			res[0] += 1
		elif i.lower() != i:
			res[1] += 1
		else:
			res[2] += 1
print "Uppercase " + str(res[1])
print "Lowercase " + str(res[0])
print "Other " + str(res[2])
import math
a = raw_input()
b = a.split(" ")
b = [float(i) for i in b]
if (b[1] ** 2 - 4 * b[0] * b[2]) < 0:
	print "It has complex Roots!"
	exit()
pos = (-b[1] + math.sqrt(b[1] ** 2 - (4 * b[0] * b[2]))) / (2 * b[0])
neg = (-b[1] - math.sqrt(b[1] ** 2 - (4 * b[0] * b[2]))) / (2 * b[0])
print "x_+ = %s; x_- = %s" % (str(round(pos, 2)), str(round(neg, 2)))
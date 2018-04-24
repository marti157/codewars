c = []
for i in range(3):
	a = raw_input()
	b = [int(a[0:2]), int(a[3:5]), int(a[6:8])]
	c.append(b)
result = [c[0][0] + c[1][0] + c[2][0], c[0][1] + c[1][1] + c[2][1], c[0][2] + c[1][2] + c[2][2]]
while result[2] >= 60:
	result[2] -= 60
	result[1] += 1
while result[1] >= 60:
	result[1] -= 60
	result[0] += 1
for i in range(len(result)):
	if result[i] <= 9:
		result[i] = "0" + str(result[i])
print str(result[0]) + "h" + str(result[1]) + "m" + str(result[2]) + "s"
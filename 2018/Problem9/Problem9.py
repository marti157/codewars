prices = []
while True:
	b = []
	a = raw_input()
	if a == "-1":
		break
	b = a.split(" ")
	if b[1] == "Y":
		prices.append(float(b[0]) * 1.8)
	else:
		prices.append(float(b[0]) * 2)
for price in prices:
	print round(price, 2)
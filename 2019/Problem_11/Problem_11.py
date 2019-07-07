num, day = input().split()
decimals = str(float(num) / float(day)).split(".")[1]
if decimals[0] != "0" and decimals[1] == "0":
	print(1)
else:
	print (0)
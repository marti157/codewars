x = int(raw_input())
total = 0
for i in range(len(bin(x)[2:]) - 1):
	total += 1
print total
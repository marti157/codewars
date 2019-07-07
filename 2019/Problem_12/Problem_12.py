transports = {"Ship": 0.3, "Train": 0.32, "Road": 2.12, "Plane": 21.01}
kms = {"Ship": 23.3, "Train": 23.1, "Road": 160.1, "Plane": 1577.1}
data = []
while True:
	inp = input()
	if inp == "#":
		break
	data.append(inp)

for inp in data:
	inp = inp.split()
	transp = inp[0]
	maxkm = int(inp[1]) / transports[transp]
	emissions = maxkm * kms[transp]
	print(transp, str(round(maxkm, 1)), str(round(emissions, 1)))
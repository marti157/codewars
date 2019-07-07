h = int(input())
poscols = []
negcols = []
if h % 2 == 0:
	centercol = " " * int(((h - 2) / 2))  + "\\/"
	centercol += "\n" +  " " * int(((h - 2) / 2)) + "/\\"
else:
	centercol = " " * int(((h - 1) / 2)) + "X"
for i in range(h - 2, 0, -2):
	addtop = "\\" + " " * i + "/"
	addtop = " " * int(((h - len(addtop)) / 2)) + addtop
	poscols.append(addtop)
	addneg = "/" + " " * i + "\\"
	addneg = " " * int(((h - len(addneg)) / 2)) + addneg
	negcols.append(addneg)
if len(poscols) == 0 and len(negcols) == 0:
	print(centercol)
else:
	negcols.reverse()
	print("\n".join(poscols) + "\n" + centercol + "\n" + "\n".join(negcols))
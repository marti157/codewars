isMagicSquare = True
words = []
for i in range(5):
	words.append(input())
testWords1 = ["", "", "", "", ""]
for word in words:
	for i in range(5):
		testWords1[i] += word[i]
testWords2 = testWords1
testWords2.reverse()
for i in range(5):
	testWords2[i] = testWords2[i][::-1]
for i in range(5):
	if testWords1[i] != words[i]:
		isMagicSquare = False
	if testWords2[i] != words[i]:
		isMagicSquare = False
print("Magic Square like Sator Arepo" if isMagicSquare else "Not a Magic Square")
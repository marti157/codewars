alph = [chr(i) for i in range(97, 97 + 26)]
text = list(input().lower())
counts = {}
alph.reverse()
for char in alph:
	counts[char] = text.count(char)
for i in alph:
	print(i + " =", counts[i])
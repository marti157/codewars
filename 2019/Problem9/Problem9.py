words = input().split()
for word in words:
	word = word if word[-1] != "R" else word + "R"
	word = word if word[-1] != "r" else word + "r"
	print(word, end=" ")
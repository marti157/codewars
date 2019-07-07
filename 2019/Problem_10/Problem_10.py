forbidden = ["noob", "n00b", "n0ob", "no0b"]
alpha = [chr(i) for i in range(97, 97 + 26)]
alpha.append(" ")
alpha.append("0")
sentence = input().lower()
for i in sentence:
	if i not in alpha:
		sentence = sentence.replace(i, "")
sentence = sentence.split(" ")
def run():
	for word in sentence:
		for testing in forbidden:
			if testing == word:
				print("User is banned.")
				return
	print("User is exhibiting a friendly behaviour.")
run()

a = raw_input()
b = raw_input()
res = [i for i in a if i not in b]
print "".join(res)
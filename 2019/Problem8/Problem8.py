opts = [input(), input(), int(input())]
texts = [opts[0].replace(opts[1], input()) for i in range(opts[2])]
print("\n".join(texts))
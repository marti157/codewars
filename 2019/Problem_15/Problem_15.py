nums = input().split(" ")
res = []
for num in nums:
  num = int(num)
  series = [1, 1]
  [series.append(series[k - 1] + series[k - 2]) for k in range(2, num)]
  res.append(str(max(series)))
print(" ".join(res))
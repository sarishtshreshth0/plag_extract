n = int(input())
res = [0] * n
for i in range(1, n):
  c, s, f = map(int, input().split())
  res[i-1] += s + c
  for j in range(i-1):
    if res[j] < s:
      res[j] = s + c
    elif res[j] == s:
      res[j] += c
    else:
      if (res[j] - s) % f == 0:
        res[j] += c
      else:
        res[j] = s + (((res[j] - s) // f) + 1) * f + c
for elem in res:
  print(elem)
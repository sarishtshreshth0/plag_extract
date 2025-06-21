n, d = map(int, input().split())
sqs = set([i ** 2 for i in range(500)])
lst = []
for i in range(n):
  temp = list(map(int, input().split()))
  lst.append(temp)
cnt = 0
for i in range(n - 1):
  for j in range(i + 1, n):
    nrm = 0
    for k in range(d):
      nrm += (lst[i][k] - lst[j][k]) ** 2
    if nrm in sqs:
      cnt += 1
print(cnt)
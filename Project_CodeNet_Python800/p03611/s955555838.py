n = int(input())
a = list(map(int, input().split()))
l = [0]*(10**5+3)
for i in range(n):
  l[a[i]] += 1
  l[a[i]+1] += 1
  l[a[i]+2] += 1
max_ = 0
for e in l:
  max_ = max(max_, e)
print(max_)
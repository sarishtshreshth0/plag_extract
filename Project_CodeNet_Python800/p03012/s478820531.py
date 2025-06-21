n = int(input())

t = list(map(int, input().split()))
sum_t = sum(t)
num = sum_t
count = 0
l = []

for i in t:
  sum_t -= i
  count += i
  l.append(abs(sum_t - count))

print(sorted(l)[0])

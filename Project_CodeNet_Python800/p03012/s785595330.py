n = int(input())
lst = list(map(int, input().split()))
samin = 100000
for i in range(n - 1):
  temp = int(abs(sum(lst[:i + 1]) - sum(lst[i + 1:])))
  if temp < samin:
    samin = temp
print(samin)
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
temp = 0
work = []
result = 0
for a in A:
    temp += a
    if temp == 0:
        result += 1
    work.append(temp)
work = Counter(work)
for v in work.values():
    if v > 1:
        result += v*(v-1)//2
print(result)
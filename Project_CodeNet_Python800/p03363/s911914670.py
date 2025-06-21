from collections import Counter
n = int(input())
A = [0]
for i in map(int,input().split()):
    A.append(A[-1]+i)
ans = 0
B = Counter(A)
for i in B.values():
    if i >= 2:
        ans += int(i*(i-1)/2)
print(ans)
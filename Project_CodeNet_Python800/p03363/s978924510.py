from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = [0]
for i in A:
    B.append(B[-1] + i)
B_C = Counter(B)
ans = 0
for key, value in B_C.items():
    ans += value * (value-1) // 2
print(ans)


import collections
N = int(input())
A = [int(i) for i in input().split()]

S = [0]
for a in A:
    S.append(S[-1]+a)

C = collections.Counter(S)

ans = 0
for v in C.values():
    if v >= 2:
        ans += v*(v-1)//2
print(ans)

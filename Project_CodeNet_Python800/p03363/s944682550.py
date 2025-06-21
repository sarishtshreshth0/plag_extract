from collections import Counter

N = int(input())
A = list(map(int, input().split()))
clm = [0]
tot = 0
for a in A:
    tot += a
    clm.append(tot)

def cmb(a):
    return a * (a - 1) // 2 

ans = 0

for a in Counter(clm).values():
    ans += cmb(a)

print(ans)
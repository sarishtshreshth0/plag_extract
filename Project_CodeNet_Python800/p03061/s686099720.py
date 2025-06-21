from math import gcd
n = int(input())
A = list(map(int, input().split()))

# 以降のGCD
left_gcds = [A[0]]
for a in A[1:]:
    left_gcds.append(gcd(left_gcds[-1], a))

right_gcds = [A[-1]]
for a in A[:n-1][::-1]:
    right_gcds.append(gcd(right_gcds[-1], a))
right_gcds.reverse()

ans = 0
for i in range(n):
    if i == 0:
        tmp = right_gcds[i+1]
    elif i == n-1:
        tmp =left_gcds[i-1]
    else:
        tmp = gcd(left_gcds[i-1], right_gcds[i+1])
    ans = max(ans, tmp)
print(ans)

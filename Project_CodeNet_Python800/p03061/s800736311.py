import fractions
N = int(input())
A = [int(i) for i in input().split()]

GCD_l = [A[0]]
for i in range(1, N-1):
    GCD_l.append(fractions.gcd(GCD_l[-1], A[i]))

A = A[::-1]
GCD_r = [A[0]]
for i in range(1, N-1):
    GCD_r.append(fractions.gcd(GCD_r[-1], A[i]))
GCD_r = GCD_r[::-1]

# print(GCD_l, GCD_r)

ans = 1
for i in range(N):
    if i == 0:
        ans = max(ans, GCD_r[0])
    elif i == N-1:
        ans = max(ans, GCD_l[N-2])
    else:
        ans = max(ans, fractions.gcd(GCD_l[i-1], GCD_r[i]))
print(ans)

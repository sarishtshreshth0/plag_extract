n = int(input())
A = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


L = [A[0]]
for a in A[1:]:
    L.append(gcd(L[-1], a))

R = [A[-1]]
for a in reversed(A[:-1]):
    R.append(gcd(R[-1], a))
R.reverse()

ans = max(L[-2], R[1])
# i番目を使わない
for i in range(1, n-1):
    x = gcd(L[i-1], R[i+1])
    if ans < x:
        ans = x
print(ans)
a, b, c, d = map(int, input().split())
n = int(input())

A = [4*a, 2*b, c]
t = 0
if min(A) * 2 > d:
    t = n//2 * d
    n = n - (n//2)*2

t += n * min(A)

print(t)
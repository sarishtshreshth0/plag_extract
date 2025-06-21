import sys
def I(): return int(sys.stdin.readline().rstrip())

N = I()

A = [0]*10  # A[i] = i桁の七五三数の個数
for i in range(1,10):
    A[i] = 3**i-3*2**i+3

d = len(str(N))  # Nの桁数
ans = sum(A[i] for i in range(1,d))  # d桁未満の七五三数の個数
B = []  # d桁の七五三数list

from itertools import product

for a in list(product(['3','5','7'],repeat=d)):
    if len(set(a)) == 3:
        b = ''
        for i in range(d):
            b += a[i]
        B.append(int(b))

print(ans+sum(n <= N for n in B))

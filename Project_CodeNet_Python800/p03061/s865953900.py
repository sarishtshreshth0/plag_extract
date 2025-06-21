from fractions import gcd
n = int(input())
a = list(map(int,input().split()))
a = sorted(a)
"""
あるn以外の最大公約数が, 最大になる組み合わせ
7 6 8 -> gcd(7,6)=1, gcd(6,8)=2 gcd(7,8)=1
12 15 18 -> gcd(12,15)=3, gcd(15,18)=3, gcd(12, 18)=6
1 2 4 6 -> 2,4,6のやつがでかい
"""
l = [0 for _ in range(n+1)]
tmp = 0
for i in range(n):
	tmp = gcd(tmp, a[i])
	l[i+1] = tmp
r = [0 for _ in range(n+1)]
a = a[::-1]
tmp = 0
for i in range(n):
	tmp = gcd(tmp, a[i])
	r[n-i-1] = tmp

m=[gcd(l[i],r[i+1]) for i in range(n)]
print(max(m))
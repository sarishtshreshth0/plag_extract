q, h, s, d = map(int, input().split())
n = int(input())

if n%2 == 0:
    print(min(n*4*q, n*2*h, n*s, n//2*d))
else:
    print(min((n-1)*4*q, (n-1)*2*h, (n-1)*s, (n-1)//2*d) + min(4*q, 2*h, s))
q, h, s, d = map(int, input().split())
n =int(input())
ans = min([4*n*q, 2*n*h, n*s, (n//2)*d+(n%2)*min(4*q, 2*h, s)])
print(ans)

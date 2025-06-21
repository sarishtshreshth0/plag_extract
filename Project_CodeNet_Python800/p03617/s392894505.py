q, h, s, d = map(int, input().split())
n = int(input())
if min(q*8, h*4, s*2)<=d:
    print(min(q*4, h*2, s)*n)
else:
    print(n//2*d+min(q*4, h*2, s)*(n%2))
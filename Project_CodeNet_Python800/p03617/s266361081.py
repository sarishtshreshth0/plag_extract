q,h,s,d = map(int,input().split())
n = int(input())

d = min(d,s*2,h*4,q*8)
s = min(s,h*2,q*4)

yen = 0

yen += (n//2)*d
yen += (n%2)*s

print(yen)
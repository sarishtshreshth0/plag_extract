q,h,s,d = map(int, input().split())
n = int(input())
q*=4
h*=2
one = min(q,h,s)
c1 = n//2*d + n%2*one
c2 = n*one
print(min(c1,c2))

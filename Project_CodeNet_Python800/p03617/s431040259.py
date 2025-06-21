q,h,s,d = map(int,input().split())
n = int(input())
q1 = q*4
h1 = h*2
q2 = q*8
h2 = h*4
s2 = s*2
b1 = 0
b2 = 0

if q1 <= h1 and q1 <= s:
    b1 = q1
elif h1 <= q1 and h1 <= s:
    b1 = h1
else:
    b1 = s


if  q2 <= h2 and q2 <= s2 and q2 <= d:
    b2 = q2
elif h2 <= q2 and h2 <= s2 and h2 <= d:
    b2 = h2
elif s2 <= q2 and s2 <= h2 and s2 <= d:
    b2 = s2
else:
    b2 = d

cnt1 = 0
cnt2 = 0

if b1*2 > b2:
    cnt1 = n//2
    cnt2 = n%2
    print((b2*cnt1)+(b1*cnt2))
else:
    print(b1*n)

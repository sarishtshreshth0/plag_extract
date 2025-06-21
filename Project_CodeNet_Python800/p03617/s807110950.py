q,h,s,d = map(int,input().split())
n = int(input())

min2 = min(q*8,h*4,s*2,d)
min1 = min(q*4,h*2,s)

if 2*min1 < min2 or n == 1:
    print(n*min1)
else:
    if n%2:
        print((n//2)*min2+min1)
    else:
        print((n//2)*min2)
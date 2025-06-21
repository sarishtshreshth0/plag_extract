n = int(input())
d = list(map(int,input().split()))
m = max(d)
if(d[0] != 0 or m >= n):
    print(0)
else:
    s = [0] * (m+1)
    for i in d:s[i] += 1
    if(0 in s or s[0] != 1):
        print(0)
    else:
        t = 1
        for i in range(1,m+1):
            t *= s[i-1]**s[i]
            t %= 998244353
        print(t)

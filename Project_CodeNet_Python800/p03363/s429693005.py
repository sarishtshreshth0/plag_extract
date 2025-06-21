n = int(input())
a = list(map(int,input().split()))
s = [0] * (n+1)
for i in range(n):
    s[i+1] = a[i]+s[i]
s.sort()
ans = 0
x = s[0]
y = 0
for i in range(1,n+1):
    if x != s[i]:
        ans += (1+y)*y//2
        x = s[i]
        y = 0
    else:
        y += 1
print(ans+(1+y)*y//2)
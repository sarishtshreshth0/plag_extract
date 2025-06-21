n = int(input())
ans = 10**100
for a in range(1,int(n**(0.5))+2):
    if n%a == 0:
        b = n//a
        f = len(str(b))
        ans = min(ans,f)
print(ans)
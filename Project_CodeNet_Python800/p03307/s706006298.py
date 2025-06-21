n = int(input())
ans = 2*n

if n%2 != 0:
    print(ans)
else:
    print(min(ans,n))
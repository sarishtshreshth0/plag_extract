N = int(input())
ans = 0
if N <= 2:
    ans = 2
else:
    if N%2 == 0:
        ans = N
    else:
        ans = N*2
print(ans)
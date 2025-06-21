N = int(input())
ans = 10
for i in range(1,10**5+1):
    if N % i == 0:
        j = N//i
        ans = min(ans, max(len(str(j)), len(str(i))))
print(ans)
import math
N = int(input())
ans = len(str(N))
for k in range(2,math.floor(math.sqrt(N))+1):
    if N % k == 0:
        ans = min(ans,max(len(str(k)),len(str(N//k))))
print(ans)

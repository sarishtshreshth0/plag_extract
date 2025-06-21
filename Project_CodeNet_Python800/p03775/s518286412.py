from math import sqrt
n = input()

ans = len(n)
N = int(n)

for A in range(1,int(sqrt(N))+1):
    if N%A == 0:
        ans = min(ans,len(str(N//A)))


print(ans)
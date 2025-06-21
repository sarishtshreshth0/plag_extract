import math

N=int(input())

L=int(math.sqrt(N))

for a in range(L+1,0,-1):
    if N%a==0:
        ans1=len(str(a))
        ans2=len(str(str(N//a)))
        print(max(ans1,ans2))
        exit()


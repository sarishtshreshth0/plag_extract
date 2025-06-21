N=int(input())

L=int(N**0.5)

for a in range(L+1,0,-1):
    if N%a==0:
        ans1=len(str(a))
        ans2=len(str(N//a))
        print(max(ans1,ans2))
        exit()


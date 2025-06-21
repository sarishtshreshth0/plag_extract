#n = int(input())
#n,k = map(int,input().split())
#x = list(map(int,input().split()))


N = int(input())
D = list(map(int,input().split()))

cnt = [0 for i in range(N)]

flg = 1
if D[0]!=0:
    flg = 0
for i in range(N):
    if D[i]==0 and i!=0:
        flg = 0
    else:
        cnt[D[i]] += 1

ans = 1
mod = 998244353
flg2 = 1
for i in range(1,N):
    if cnt[i]>0 and flg2:
        ans *= cnt[i-1]**cnt[i]
        ans %= mod
    elif cnt[i]>0 and (not(flg2)):
        flg = 0
    else:
        flg2 = 0
print(ans*flg)
    
    

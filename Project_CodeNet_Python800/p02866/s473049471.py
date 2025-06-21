n = int(input())
count = [0]*n
ans = 1
flag = True
for d in map(int,input().split()):
    if flag:
        if d!=0:
            print(0)
            exit()
        flag = False
    count[d] += 1
for i in range(1,n):
    if count[0]!=1:
        ans = 0
        break
    if count[i]==0:
        if any(k!=0 for k in count[i:]):
            ans = 0
        break
    ans *= (count[i-1]**count[i])%998244353
    
print(ans%998244353)
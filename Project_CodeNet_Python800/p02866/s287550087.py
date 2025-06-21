n = int(input())
d = list(map(int,input().split()))
MOD = 998244353
if d[0] != 0:
    print(0)
    exit()
d.sort()
for i in range(1,n):
    if d[i] - d[i-1] > 1:
        print(0)
        exit()
    if d[i] == 0:
        print(0)
        exit()
count = 1
tmp = 1
ans = 1
for i in range(2,n):
    if d[i] != d[i-1]:
        ans *= pow(tmp,count,MOD)
        #print(tmp,count)
        tmp = count
        count = 1
    else:
        count+=1
ans *= pow(tmp,count,MOD)
ans %= MOD
#print(tmp,count)
print(ans)
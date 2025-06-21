MOD = 998244353
N = int(input())
D = list(map(int,input().split()))
lis = [0] * (max(D)+1)
if D[0] != 0:
    print(0)
    exit()
for i in D:
    lis[i] += 1
if lis[0] == 0 or lis[0] > 1:
    print(0)
    exit()


ans = 1
for i in range(1,len(lis)):
    ans *= pow(lis[i-1],lis[i], MOD)
    ans %= MOD
print(ans)

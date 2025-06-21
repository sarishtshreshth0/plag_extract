import collections
mod = 998244353

N = int(input())
D = list(map(int,input().split()))

if D[0] != 0 or 0 in D[1:]:
    print(0)
    exit()

Dep = collections.Counter(D)
values, counts = zip(*Dep.most_common())
#print(values)
#print(counts)
#print(Dep)
ans = 1
for i in range(1,len(values)):
    if Dep[i-1] == 0:
        ans = 0
    ans *= pow(Dep[i-1],Dep[i], mod)
    #print(i,Dep[i])
    ans %= mod
print(ans)

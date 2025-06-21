MOD = 998244353
N = int(input())
D = list(map(int, input().split()))
D_2 = [0]*(max(D)+1)
for i in D:
    D_2[i] += 1
ans = 1 if D_2[0] == 1 and D[0] == 0 else 0
for i in range(1,max(D)+1):
    ans *= D_2[i-1]**D_2[i]
    ans %= MOD
print(ans)

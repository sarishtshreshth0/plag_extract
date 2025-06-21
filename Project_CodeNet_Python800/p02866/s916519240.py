N = int(input())
D = list(map(int, input().split()))
ans = 0
if not D[0] == 0 or not D.count(0) == 1:
    print(0)
else:
    co = [0] * (max(D)+1)
    for i in D:
        co[i] += 1
    ans = 1
    for i in range(2, max(D)+1):
        ans = ans * (co[i-1]**co[i]) % 998244353
    print(ans)
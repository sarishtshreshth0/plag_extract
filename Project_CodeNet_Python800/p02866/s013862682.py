n = int(input())
d = list(map(int, input().split()))
if d[0]!=0:
    print(0)
    exit()
node = [0]*(max(d)+1)
for i in d:
    node[i] += 1
if node[0]>1:
    print(0)
    exit()
ans = 1
for i in range(len(node)-1):
    ans *= node[i]**node[i+1]
    ans %= 998244353
print(ans)
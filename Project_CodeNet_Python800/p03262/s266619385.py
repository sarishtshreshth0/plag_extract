from math import gcd
n,start = map(int,input().split())
x_ls = list(map(int, input().split()))
diff_ls = [0] * n

for i in range(n):
    diff_ls[i] = abs(start-x_ls[i])

ans = diff_ls[0]
for i in range(1,n):
    ans = gcd(ans,diff_ls[i])

print(ans)
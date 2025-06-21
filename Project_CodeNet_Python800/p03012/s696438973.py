n = int(input())
w = list(map(int,input().split()))
s = sum(w)
g = 10**5
cnt = 0
for i in range(n):
    cnt += w[i]
    if abs(s-cnt*2) <= g:
        g = abs(s-cnt*2)
        ans = abs(s-cnt*2)
print(ans)
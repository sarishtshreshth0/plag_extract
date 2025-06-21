def con2(n):
    return n*(n-1)//2

n = int(input())
a = list(map(int, input().split()))
s = [0] * (n+1)
dic = {0:1}
for i in range(1, n+1):
    s[i] = s[i-1] + a[i-1]
    if not s[i] in dic:
        dic[s[i]] = 1
    else:
        dic[s[i]] += 1
ans = 0
#print(s)
#print(dic)
for key in dic:
    if dic[key] == 1:
        continue
    else:
        ans += con2(dic[key])

print(ans)

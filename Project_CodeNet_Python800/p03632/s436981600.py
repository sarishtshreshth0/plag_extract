a,b,c,d = map(int,input().split())
x = [0]*(202)
x[a] += 1
x[b] -= 1
x[c] += 1
x[d] -= 1
for i in range(201):
    x[i+1] += x[i]
ans = 0
for i in range(202):
    if x[i] == 2:
        ans += 1
print(ans)
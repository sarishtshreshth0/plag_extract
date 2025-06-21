n = int(input())
a = list(map(int,input().split()))

b = [0]

for i in a:
    b.append(b[-1] + i)

d = {}
ans = 0

for i in b:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for k,v in d.items():
    ans += v * (v-1) // 2

print(ans)

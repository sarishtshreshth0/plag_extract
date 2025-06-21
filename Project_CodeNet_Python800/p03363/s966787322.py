n = int(input())
a = list(map(int, input().split()))
s = [0]
for i in a:
    s.append(i+s[-1])
b = sorted(s)
c = [[b[0], 1]]
for i in range(1, n+1):
    if b[i] == c[-1][0]:
        c[-1][1] += 1
    else:
        c.append([b[i], 1])
ans = 0
for i in c:
    ans += (i[1]*(i[1]-1))//2
print(ans)
n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    a.append(a[i] + 1)
    a.append(a[i] - 1)
a = sorted(a)
ans = []
c = 1
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        c += 1
    else:
        ans.append(c)
        c = 1
print(max(ans))

A, B, C, D = map(int, input().split())

a = []
for i in range(A, B):
    a.append(i)

b = []
for  i in range(C, D):
    b.append(i)

ans = 0
for i in a:
    if i in b:
        ans += 1

print(ans)

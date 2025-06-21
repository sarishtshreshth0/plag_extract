import itertools

n = int(input())

a =["3","5","7"]
l = []
for i in range(3,10):
    for j in itertools.product(a,repeat=i):
        l.append(j)

ans = 0
for i in l:
    if int("".join(i)) <= n and i.count("3") >= 1 and i.count("5") >= 1 and i.count("7") >= 1:
        ans += 1

print(ans)
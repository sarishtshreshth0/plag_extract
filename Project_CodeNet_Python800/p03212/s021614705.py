from itertools import product
n = int(input())
i = len(str(n))

cnt = 0
for j in range(3, i+1):
    for k in product(["3", "5", "7"], repeat=j):
        if len(set(k)) != 3:
            continue
        if int("".join(k)) <= n:
            cnt += 1

print(cnt)
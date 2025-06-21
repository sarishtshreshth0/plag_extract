from itertools import product
N = int(input())
ans = 0
for i in range(3, 10):
    l = list(product(["3","5","7"],repeat=i))
    for j in l:
        if len(set(j)) == 3:
            if int("".join(list(j))) <= N:
                ans += 1
print(ans)

from itertools import product
n = int(input())
ans = 0
for l in range(1, 10):
    for b in product('753', repeat=l):
        if len(set(iter(b))) == 3 and int(''.join(b)) <= n:
            ans += 1
print(ans)

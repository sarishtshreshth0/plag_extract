from itertools import product

n = int(input())

ans = 0
for i in range(1, 10):
    for pat in product("357", repeat=i):
        num = "".join(pat)
        st = set(num)
        if int(num) <= n and st == {"3", "5", "7"}:
            ans += 1

print(ans)

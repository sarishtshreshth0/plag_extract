import itertools

N = int(input())
ans = 0
list_753 = []

for i in range(10):
    list_753 += list(itertools.product("753",repeat = i))

for num in list_753:
    if len(set(num)) == 3 and int("".join(num)) <= N:
        ans += 1

print(ans)
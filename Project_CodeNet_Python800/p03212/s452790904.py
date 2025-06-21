from itertools import product

N = int(input())

_357 = {'3', '5', '7'}

ans = 0
for r in range(3, len(str(N)) + 1):
    for numbers in product(('3', '5', '7'), repeat=r):
        if set(numbers) == _357 and int(''.join(numbers)) <= N:
            ans += 1

print(ans)

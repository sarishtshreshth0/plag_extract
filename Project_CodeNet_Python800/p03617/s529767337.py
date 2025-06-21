Q, H, S, D = map(int, input().split())
N = int(input())

price = [(8 * Q, 0.25), (4 * H, 0.5), (2 * S, 1.0), (D, 2.0)]
price.sort()

res = 0
if N % 2 == 0:
    res += N // 2 * price[0][0]
else:
    res += (N - 1) // 2 * price[0][0]
    for p in price:
        if p[1] == 2.0:
            continue
        res += p[0] // 2
        break

print(int(res))

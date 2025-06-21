# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

Price = list(map(int, input().split()))
Volume = [0.25, 0.5, 1, 2]
Pper = [p/v for (p, v) in zip(Price, Volume)]
N = int(input())

ans = 0
n = Pper.index(min(Pper))
if n != 3:
    ans = int(N/Volume[n]) * Price[n]
else:
    ans = N//2 * Price[3]
    m = Pper.index(min(Pper[:3]))
    nokori = N % 2
    ans += int(nokori/Volume[m]) * Price[m]

print(ans)

# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

H, W = map(int, input().split())
ans = 0
if H == 1 or W == 1:
    ans = 1
else:
    ans = (-H//2) * (-W//2) + (H//2) * (W//2)
print(ans)

# print(-(-H // 2))
# print(-(-W // 2))
# print(H // 2)
# print(W//2)

# print(4 * 2 + 3 * 1)

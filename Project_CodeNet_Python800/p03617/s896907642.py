Q, H, S, D = map(int, input().split())
N = int(input())
l_1 = min((Q * 4), (H * 2), (S * 1))
l_2 = min((Q * 8), (H * 4), (S * 2), (D * 1))
ans = 0

if N == 1:
    ans = int(l_1)
elif N % 2 == 0:
    ans = int(l_2 * (N // 2))
else:
    ans = int(((N - 1) // 2) * l_2 + l_1)
print(ans)
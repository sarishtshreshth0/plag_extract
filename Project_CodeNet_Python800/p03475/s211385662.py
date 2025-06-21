import numpy as np

N = int(input())
C, S, F = [], [], []
for _ in range(N - 1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)
# cumsum_C = np.array(C)[::-1].cumsum()
# print(f'{cumsum_C=}')

for i in range(N):
    x = 0
    for j in range(i, N - 1):
        if S[j] > x:
            x = S[j]
        else:
            # S[j] + a * F[j] > x
            a = ((x - S[j]) + (F[j] - 1)) // F[j]
            x = S[j] + F[j] * a
        x += C[j]
        # print(f'{x=}')
    print(x)
# T = [0] * (N - 1)
# T[-1] = C[-1] + S[-1]
# for i in range(N - 2, -1, -1):
#     if C[i] + S[i] > S[i + 1]:
#         T[i] = C[i] + S[i]
#     else:
#         T[i] = C[i] + S[i] + C[i + 1]
# 後ろから考えていき、その駅の始発に乗れない場合はプラスで待ち時間を加える
# 後ろからのCのcumsumがいる
# 12 24 6 -> 12 + 24 > 16 -> 12 + 24 + 0 + 52 + 99
# 52 16 4 -> 52 + 16 > 2 -> 52 + 16 + 99
# 99 2 2 -> 101

# やっぱりDPっぽくする必要ありそう？

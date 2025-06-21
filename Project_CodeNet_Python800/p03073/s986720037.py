S = input()
N = len(S)

# 0101...にする場合
cnt1 = 0
for i in range(len(S)):
    if S[i] != str(i % 2):
        cnt1 += 1

# 1010...にする場合
cnt2 = 0
for i in range(len(S)):
    if S[i] != str((i + 1) % 2):
        cnt2 += 1

print(min(cnt1, cnt2))

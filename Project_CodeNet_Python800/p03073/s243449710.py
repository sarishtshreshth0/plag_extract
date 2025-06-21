S = input()
n = len(S)
pattern1 = [i % 2 for i in range(n)]
pattern2 = [i % 2 for i in range(1, n+1)]
ans1 = 0
ans2 = 0
for i in range(n):
    s = S[i]
    if s == str(pattern1[i]):
        ans1 += 1
    if s == str(pattern2[i]):
        ans2 += 1
else:
    ans = min(ans1, ans2)
print(ans)

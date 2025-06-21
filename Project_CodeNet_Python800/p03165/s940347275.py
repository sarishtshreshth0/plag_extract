import numpy as np
s = np.array(list(input()))
t = np.array(list(input()))
dp = np.zeros((len(s)+1, len(t)+1), dtype=int)

equal = s[:, None] == t[None, :]

for i in range(len(s)):
    dp[i+1, 1:] = np.maximum(dp[i, :-1]+equal[i], dp[i, 1:])
    dp[i+1] = np.maximum.accumulate(dp[i+1])

i = len(s)
j = len(t)
ans = []

while i>0 and j>0:
    if s[i-1] == t[j-1]:
        ans.append(s[i-1])
        i -= 1
        j -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else :
        j -= 1

print(''.join(ans[::-1]))

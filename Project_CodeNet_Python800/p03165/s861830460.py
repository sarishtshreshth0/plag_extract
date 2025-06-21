import numpy as np
s = np.array(list(input()))
t = np.array(list(input()))
slen = len(s)
tlen = len(t)

dp = np.zeros((slen+1,tlen+1),dtype=int)

equal = (s[:,None] == t[None,:])
for i in range(slen):
    dp[i+1][1:] = np.maximum(dp[i][1:], dp[i][:-1] + equal[i])
    dp[i+1] = np.maximum.accumulate(dp[i+1])

ans = []
while dp[slen,tlen] != 0:
    if s[slen-1] == t[tlen-1]:
        ans.append(s[slen-1])
        slen -= 1
        tlen -= 1
    elif dp[slen,tlen] == dp[slen-1,tlen]:
        slen -= 1
    else:
        tlen -= 1
print("".join(ans[::-1]))
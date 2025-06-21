s= input()
t = input()
ls = len(s)
lt = len(t)
dp = [[0 for _ in range(lt+1) ]  for _ in range(ls+1)] #dp[i][j] sがi文字目,tがj文字目まででのLCS
for ids in range(1,ls+1):
    for idt in range(1,lt + 1):
        #一致してたら文字を足す
        if s[ids-1] == t[idt-1]:
            dp[ids][idt] =dp[ids-1][idt-1] + 1
        #違っていたら、長い方の文字を採用
        elif s[ids-1] != t[idt-1]:
            if dp[ids][idt-1] >= dp[ids-1][idt]:
                dp[ids][idt] = dp[ids][idt-1]
            else:
                dp[ids][idt] = dp[ids-1][idt]
ans = ''
num=dp[-1][-1]
ids = ls;idt=lt
while num:
    if dp[ids][idt] == dp[ids][idt-1]:
        idt -= 1
    elif dp[ids][idt] == dp[ids-1][idt]:
        ids -=1
    elif dp[ids][idt] ==dp[ids-1][idt-1] + 1:
        ans += s[ids-1]
        num -=1
        idt -= 1
        ids -=1
print(ans[::-1])


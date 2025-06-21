#https://atcoder.jp/contests/abc143/tasks/abc143_c
N =int(input())
S =str(input())
cnt = 1
moji = S[0]
for i in range(1,N):
    if S[i] != moji:
        cnt += 1
        moji = S[i]

print(cnt)    
    
    



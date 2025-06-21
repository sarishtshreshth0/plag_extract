S = list(input())

ans = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        pass
    else:
        x = S[i+1]
        if x == '0':
            S[i+1] = '1'
        else:
            S[i+1] = '0'
        ans += 1

print (ans)

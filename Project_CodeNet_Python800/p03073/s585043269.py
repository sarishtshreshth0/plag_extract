S = input()
cnt = 0
for i in range(len(S)):
    if (i%2==0 and S[i] == '0') or (i%2==1 and S[i] == '1'):
        cnt += 1
print(min(len(S)-cnt,cnt))
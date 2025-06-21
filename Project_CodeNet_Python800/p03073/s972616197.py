S = input()

if S[0] == '0':
    A = '01' * len(S)
else:
    A = '10' * len(S)
    
cnt = 0
for i in range(len(S)):
    if S[i] != A[i]:
        cnt += 1
        
print(cnt)
N = int(input())
S = input()
S = list(S)

d = []
for n in range(1, N):
    if S[n-1] == S[n]:
        d.append(n)

cnt = 0
for i in d:
    i -= cnt
    del S[i]
    cnt += 1
    
print(len(S))
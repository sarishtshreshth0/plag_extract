N = int(input())
S = input()
S = [i for i in S]

cnt = 1
Cnt = []

for i in range(1, N):
    if S[i]==S[i-1]:
        cnt += 1
    elif S[i]!=S[i-1]:
        Cnt.append(cnt)
        cnt = 1
Cnt.append(cnt)
print(len(Cnt))
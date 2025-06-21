N = int(input())
S = input()

cnt = 1
col = S[0]

for c in S:
    if(c != col):
        cnt += 1
        col = c

print(cnt)
N, A, B = map(int, input().split())
S = list(input())

cnt = A + B
Bcnt = B

for i in range(len(S)):
    if S[i] == 'a' and cnt > 0:
        print('Yes')
        cnt -= 1
    elif S[i] == 'b' and cnt > 0 and Bcnt > 0:
        print('Yes')
        cnt -= 1
        Bcnt -= 1
    else:
        print('No')
N, A, B = map(int, input().split())
S = list(input())
cnt = 0
b_cnt = 0

for i in range(N):
    if S[i] == 'a':
        S[i] = 'Yes'
        cnt += 1
    elif S[i] == 'b':
        if b_cnt >= B:
            continue
        S[i] = 'Yes'
        cnt += 1
        b_cnt += 1

    if cnt == A + B:
        break

ans = ['No' if j != 'Yes' else j for j in S]

for k in range(N):
    print(ans[k])
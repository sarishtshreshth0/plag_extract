N, A, B = map(int, input().split())
S = list(input())
a = 0 # 予選通過人数
b = 0 # 海外
for i in range(N):
    ans = 'No'
    if S[i] == 'a':
        if a < A + B:
            ans = 'Yes'
            a += 1
    elif S[i] == 'b':
        if a < A + B and b < B:
            ans = 'Yes'
            a += 1
            b += 1
    print(ans)
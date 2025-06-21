N, A, B = map(int, input().split())
S = input()
tol = 0
bcnt = 0
ans = []
for c in S:
    if c == 'a':
        if tol < (A+B):
            tol += 1
            ans.append('Yes')
        else:
            ans.append('No')
    elif c == 'b':
        bcnt += 1
        if tol < (A+B) and bcnt <= B:
            tol += 1
            ans.append('Yes')
        else:
            ans.append('No')
    else:
        ans.append('No')
        continue
for s in ans:
    print(s)
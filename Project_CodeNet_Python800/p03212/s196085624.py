from collections import Counter
n = int(input())
ans = 0
def dfs(A):
    if A and int(A) > n:
        return
    if len(A) >= 3:
        c = Counter(A)
        is753 = True
        for i in ['7','5','3']:
            if c[i] < 1:
                is753 = False
        if is753:
            global ans 
            ans += 1
    for nex in ['7','5','3']:
        A += nex
        dfs(A)
        A = A[:-1]
dfs('')
print(ans)
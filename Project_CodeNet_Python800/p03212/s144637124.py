N = input()

def dfs(A):
    if int(A) > int(N):
        return 0
    if all(A.count(c) for c in "753") >0:
        ans = 1
    else:
        ans = 0
        
    for i in "357":
        A += i
        ans += dfs(A)
        A = A[:-1]
        
    return ans

print(dfs("0"))
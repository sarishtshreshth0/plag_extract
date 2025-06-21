n = int(input())
B = []
def dfs(A):
  x = int(''.join(A))
  if x <= n:
    if '7' in A and '5' in A and '3' in A:
      B.append(x)
    dfs(A + ['7'])
    dfs(A + ['5'])
    dfs(A + ['3'])

dfs(['0'])
print(len(B))
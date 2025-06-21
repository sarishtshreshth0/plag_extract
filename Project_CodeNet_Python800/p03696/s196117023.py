from collections import deque

N = int(input())
S = input()

ans = deque([])
emp = deque([])
for s in S[::-1]:
    if s == ")":
        ans.append('(')
    else:
        if ans:
            ans.pop()
        else:
            emp.append(')')
ans = list(ans)
emp = list(emp)
print("".join(ans)+S+"".join(emp))
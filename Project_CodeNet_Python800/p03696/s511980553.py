n = int(input())
s = input()
stack = []
cntLeft = 0
cntRight = 0
for ss in s:
    if ss == '(':
        stack.append('(')
    else:
        if len(stack) > 0:
            stack.pop()
        else:
            cntLeft += 1
cntRight = len(stack)
ans = ''
for i in range(cntLeft):
    ans += '('
ans += s
for i in range(cntRight):
    ans += ')'
print(ans)

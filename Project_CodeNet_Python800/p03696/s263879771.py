n = int(input())
data = [c for c in input()]
stack = []
ans = ''
for c in data:
    if c == '(':
        stack.append(c)
        ans += '('
    else:
        if len(stack) == 0 or stack.pop() != '(':
            ans = '(' + ans + c
        else:
            ans += ')'
ans += ')'*len(stack)

print(ans)
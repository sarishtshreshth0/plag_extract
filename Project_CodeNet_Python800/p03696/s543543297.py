n = int(input())
s = list(input())
stack = []
for i in range(n):
    if s[i] == "(":
        stack.append("(")
    elif len(stack) == 0 or stack[-1] == ")":
        stack.append(")")
    else:
        stack.pop()
stack = sorted(stack, reverse=True)
idx = 0
while idx < len(stack):
    if stack[idx] == "(":
        break
    else:
        print("(", end="")
    idx+=1
for ch in s:
    print(ch, end="")
for i in range(idx, len(stack)):
    print(")", end="")





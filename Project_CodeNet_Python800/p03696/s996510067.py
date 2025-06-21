import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

stack = []
for s_i in S:
    if not stack:
        stack.append(s_i)
    elif stack[-1] == "(" and  s_i == ")":
        stack.pop()
    else:
        stack.append(s_i)

# 余っている左、右のカッコの数 
left = 0
right = 0
for s_i in stack:
    if s_i == ")":
        right += 1
    else:
        left += 1

print("(" * right + S + ")" * left)
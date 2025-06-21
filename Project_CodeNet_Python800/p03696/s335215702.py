N = int(input())
S = input()
l = 0
r = 0
for c in S:
    if c == '(':
        l += 1
    else:
        if l != 0:
            l -= 1
        else:
            r += 1
print('('*r + S + ')'*l)
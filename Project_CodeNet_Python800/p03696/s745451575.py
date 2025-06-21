N = int(input())
S = input()

b = 0
e = 0
for s in S:
    if s == ')':
        e += 1
    else:
        b += 1
    S = '(' * max(e-b, 0) + S
    b += max(e-b, 0)
S += ')' * max(b-e, 0)
print(S)

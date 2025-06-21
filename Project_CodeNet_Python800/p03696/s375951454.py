n = int(input())
S = input()
leftstack = 0

remrights = 0
for s in S:
    if s == '(':
        leftstack += 1
    else:
        if leftstack > 0:
            leftstack -= 1
        else:
            remrights += 1
print('('*remrights + S + ')'*leftstack)


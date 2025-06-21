n = int(input())
s = input()

nopen = 0
sl = ''
sr = ''

for c in s:
    if c == '(':
        nopen += 1
    else:
        if nopen == 0:
            sl += '('
        else:
            nopen -= 1

nopen = sum([1 if c == '(' else -1 for c in sl + s])
sr = ')' * nopen


print(sl + s + sr)

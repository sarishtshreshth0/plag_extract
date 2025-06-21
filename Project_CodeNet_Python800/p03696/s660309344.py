n = int(input())
s = input()
i = 0
mi = 0
for c in s:
    if c=='(':
        i += 1
    else:
        i -= 1
    mi = min(mi, i)
ans = '('*(-mi) + s + ')'*(i-mi)
print(ans)
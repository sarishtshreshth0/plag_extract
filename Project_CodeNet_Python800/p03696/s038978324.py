n = int(input())
s = input()
c = 0
d = 0
for i in range(n):
    if s[i] == '(':
        c += 1
    else:
        d += 1
used_c = [True]*n
used_d = [True]*n
for i in range(n):
    if s[i] == '(':
        for j in range(i+1, n):
            if s[j] == ')' and used_c[j]:
                c -= 1
                used_c[j] = False
                break
    else:
        for j in range(i):
            if s[j] == '(' and used_d[j]:
                d -= 1
                used_d[j] = False
                break
print('('*d+s+')'*c)

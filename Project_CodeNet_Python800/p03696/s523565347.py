n = int(input())
x = list(input())
sta = 0
left = 0
for i in range(n):
    if x[i] == '(':
        sta += 1
    else:
        if sta == 0:
            left += 1
        else:
            sta -= 1
s = []
for i in range(left):
    s.append('(')
for i in range(n):
    s.append(x[i])
for i in range(sta):
    s.append(')')
print(''.join(s))
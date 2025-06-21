n = int(input())
s = input()

m = 0
now = 0
for i in s:
    if i == ')':
        now += 1
        if m < now:
            m = now
    else:
        now -= 1

print('('*m + s + ')'*(m + 2*s.count('(') - len(s)))
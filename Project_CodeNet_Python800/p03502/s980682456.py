n = input()
l = list(n)
_sum = 0
for a in l:
    _sum += int(a)
if int(n) % _sum == 0:
    print('Yes')
else:
    print('No')
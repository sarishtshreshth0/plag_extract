n = input()

length = len(n)
s = 0
for a in range(0, length):
    s += int(n[a])

if int(n) % s == 0:
    print('Yes')
else:
    print('No')

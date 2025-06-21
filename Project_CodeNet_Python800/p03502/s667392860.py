n = int(input())
nn = list(str(n))
num = [int(i) for i in nn]
total = 0
for i in range(len(nn)):
    total += num[i]

if n % total == 0:
    print('Yes')
else:
    print('No')
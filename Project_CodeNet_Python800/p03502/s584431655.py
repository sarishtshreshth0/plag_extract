n = int(input())
l = []

for i in range(len(str(n))):
    l.append(int(str(n)[i]))

if n % sum(l) == 0:
    print('Yes')
else:
    print('No')
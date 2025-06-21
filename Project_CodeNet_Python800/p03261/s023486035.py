n = int(input())
l = []

for i in range(n):
    l.append(input())

L = set(l)

if len(l) == len(L):
    for i in range(n-1):
        if l[i][-1] != l[i+1][0]:
            print('No')
            exit()
    print('Yes')
else:
    print('No')
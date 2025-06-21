n = int(input())
w = list(input() for i in range(n))

if len(w) != len(set(w)):
    print('No')
    exit(0)

for i in range(n - 1):
    if w[i][-1] != w[i + 1][0]:
        print('No')
        exit(0)

print('Yes')
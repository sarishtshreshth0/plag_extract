
N = int(input())

total = 0
for c in str(N):
    total += int(c)

if N % total == 0:
    print('Yes')
else:
    print('No')

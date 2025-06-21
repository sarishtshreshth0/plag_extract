# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

origin = list(map(int, input().rstrip('\n')))
# print(origin)

t1 = []
t2 = []
for i in range(len(origin)):
    if i % 2 == 0:
        t1.append(0)
        t2.append(1)
    else:
        t1.append(1)
        t2.append(0)

n1 = 0
n2 = 0
for i in range(len(origin)):
    if t1[i] != origin[i]:
        n1 += 1
    if t2[i] != origin[i]:
        n2 += 1

print(min(n1, n2))

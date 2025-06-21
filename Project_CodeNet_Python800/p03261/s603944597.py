# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N = int(input())
S = []
for i in range(N):
    S.append(input().rstrip('\n'))

if len(set(S)) != N:
    print("No")
    exit()
else:
    for i in range(1, N):
        if S[i - 1][-1] != S[i][0]:
            print("No")
            exit()

print("Yes")

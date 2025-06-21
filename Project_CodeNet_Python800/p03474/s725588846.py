# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
list_n = list(map(str, input().rstrip('\n').split("-")))
# print(list_n[0])
# print(list_n[1])
if len(list_n[0]) == A and len(list_n[1]) == B:
    print("Yes")
else:
    print("No")

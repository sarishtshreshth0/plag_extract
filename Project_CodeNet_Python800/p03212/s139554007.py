import sys
sys.setrecursionlimit(10**6)

N = int(input())
V = [3, 5, 7]

li = []


def rec(curr, use):
    if curr > N:
        return
    if use == 0b111:
        li.append(curr)
    for i, b in enumerate(V):
        rec(curr * 10 + b, use | max(1, i * 2))


rec(0, 0)

print(len(li))
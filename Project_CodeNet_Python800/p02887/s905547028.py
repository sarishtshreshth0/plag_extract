from itertools import groupby
n = int(input())
s = input()
g = groupby(s)
print(len(list(g)))
from itertools import groupby
N = int(input())
S = input()
gr = list(groupby(S))
print(len(gr))

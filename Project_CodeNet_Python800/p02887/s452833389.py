from itertools import groupby
n= input()
s = input()
G = groupby(s)

print(len(list(G)))
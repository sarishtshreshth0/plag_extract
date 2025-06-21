import sys
import numpy as np
import collections as cl
import itertools as it
# import more_itertools as mit
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(100000)

n = int(readline())
w = [input().strip() for _ in range(n)]
dic = set()

for num, i in enumerate(w):
    if num == 0:
        dic.add(i)
        continue
    if i in dic or w[num-1][-1] != i[0]:
        print('No')
        sys.exit()
    dic.add(i)
print('Yes')
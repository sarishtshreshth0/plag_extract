import sys
def input():
    return sys.stdin.readline()[:-1]
import math
from itertools import permutations, combinations
from collections import deque, defaultdict

sys.setrecursionlimit(10**7)
N = int(input())
edges = [[] for _ in range(N)]
nodeinput = defaultdict(int) # (node index, node index) -> index
for i in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
    if a > b:
        a, b = b, a
    nodeinput[(a-1, b-1)] = i

seen = [0]*N
output = [0]*(N-1) # color

stack = deque()
stack.append([(0, -1)]) # node index, parent color
maxcolor = 0
while stack[0]:
    nstack = []
    cstack = stack.pop()
    #print('cstack:', cstack)
    for val in cstack:
        ni, pc = val
        seen[ni] = 1
        color = 1
        if color == pc:
            color += 1
        for edgei in edges[ni]:
            if seen[edgei] == 0:
                nstack.append((edgei, color))
                if ni > edgei: # keep: ni < edgei
                    ni, edgei = edgei, ni
                output[nodeinput[(ni, edgei)]
                ] = color
                if maxcolor < color:
                    maxcolor = color
                color += 1
                if color == pc:
                    color += 1
    stack.append(nstack)

print(maxcolor)
for out in output:
    print(out)

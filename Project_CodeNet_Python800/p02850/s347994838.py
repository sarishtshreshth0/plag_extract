#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
#import bisect
#from collections import deque
import math

sys.setrecursionlimit(10**5)

def input():
    return sys.stdin.readline().rstrip('\n')

N = int(input())
peers = [[] for _ in range(N)]
colors = [{} for _ in range(N)]
pairs = []
for _ in range(N-1):
    a,b = list(map(int, input().split()))
    a -= 1
    b -= 1
    pairs.append([a,b])
    peers[a].append(b)
    colors[a][b] = 0


def draw(node, parent_edge_color):
    _peers = peers[node]
    if len(_peers) == 0:
        return 0
    color = 1
    max_nrof_color = 1
    for peer in _peers:
        #print(node,peer,color)
        if color == parent_edge_color:
            color +=1
        colors[node][peer] = color
        max_nrof_color = max(max_nrof_color, color, draw(peer, color))
        color += 1

    return max_nrof_color


print(draw(0,0))
for a,b in pairs:
    print(colors[a][b])

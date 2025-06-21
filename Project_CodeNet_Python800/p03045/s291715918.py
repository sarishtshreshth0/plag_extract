#!/usr/bin/python3
# -*- coding: utf-8 -*-

# scipy version

import sys
from collections import deque
from array import array

import numpy

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

def input():
    return sys.stdin.readline().rstrip('\n')

##### main

N,M = list(map(int, input().split()))

#C = [[0]*N for _ in range(N)]
#
#for i in range(M):
#    a,b,c = list(map(int, input().split()))
#    C[a-1][b-1] = c

R = numpy.full(M, 0, dtype=numpy.int32)
C = numpy.full(M, 0, dtype=numpy.int32)
V = numpy.full(M, 0, dtype=numpy.int32)

for i in range(M):
    r,c,v = list(map(int, input().split()))
    R[i] = r-1
    C[i] = c-1
    V[i] = v

matrix = csr_matrix((V,(R,C)), shape=(N,N))

n = connected_components(matrix, directed=False, return_labels=False)

print(n)

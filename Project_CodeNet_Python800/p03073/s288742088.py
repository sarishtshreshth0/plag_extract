#import numpy as np
#import functools
#import operator
#from itertools import combinations as comb
#from itertools import combinations_with_replacement as comb_with
#from itertools import permutations as perm
#import collections as C #most_common

#N = int(input())
#N,M= map(int,input().split())
#P = list(map(int,input().split()))

S= str(input())
#prod = functools.partial(functools.reduce, operator.mul)
#c=np.array(A)
#p=np.prod(A)

one=[1,0]*10**5
zero=[0,1]*10**5

o=0
z=0
for i in range(len(S)):
    if one[i] != int(S[i]):
        o+=1
    if zero[i] != int(S[i]):
        z+=1

print(min(o,z))

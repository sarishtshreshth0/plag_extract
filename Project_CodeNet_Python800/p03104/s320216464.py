#import sys
#import numpy as np
#import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
a,b=map(int,input().split())
if a==b:
  print(a)
  exit()
if a==0:
  i=0
  resb=0
  while True:
    if i==0:
      if ((b+1)//2)%2==1:
        resb+=1
      i+=1
      continue
    if 2**i>b+1:
        break
    if ((b+1)%(2**i))%2==1 and ((b+1)//(2**i))%2==1:
        resb+=2**i
    i+=1
  print(resb)
  exit()
  
n_b=b.bit_length()
n_a=(a-1).bit_length()
i=0
res=0

while True:
    if i==0:
      if (a//2)%2==1:
        res+=1
      i+=1
      continue
    if 2**i>a:
        break
    if (a%(2**i))%2==1 and (a//(2**i))%2==1:
        res+=2**i
    i+=1
i=0
resb=0
while True:
  if i==0:
    if ((b+1)//2)%2==1:
      resb+=1
    i+=1
    continue
  if 2**i>b+1:
        break
  if ((b+1)%(2**i))%2==1 and ((b+1)//(2**i))%2==1:
        resb+=2**i
  i+=1
print(res^resb)
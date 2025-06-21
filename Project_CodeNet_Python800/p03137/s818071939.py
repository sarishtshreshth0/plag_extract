from collections import defaultdict
from collections import deque
import itertools
import math

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

n,m = readInts()
x = readInts()
x.sort()

if m==1:
  print(0)
  exit()

intval = []
for i in range(len(x)-1):
  intval.append(x[i+1]-x[i])
intval.sort(reverse=True)

ans = x[-1]-x[0]
for i in range(min(n-1,len(intval))):
  ans-=intval[i]

print(ans)
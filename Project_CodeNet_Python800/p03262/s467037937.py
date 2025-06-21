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

n,x = readInts()
xs = readInts()
xs.append(x)
xs.sort()

ans = xs[1]-xs[0]
for i in range(n):
  ans = math.gcd(ans,xs[i+1]-xs[i])

print(ans)
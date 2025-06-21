import sys
from collections import Counter
from collections import deque
import math
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))


n=int(input())
s=input()


i=0
c=0
while i<len(s):
    if s[i]=="(" and c<0:
        s="("*(-c)+s
        i-=c
        c=0
    elif s[i]=="(":
        c+=1
        i+=1
    else:
        c-=1
        i+=1

if c<0:
    s="("*(-c)+s
elif c>0:
    s=s+")"*c
print(s)
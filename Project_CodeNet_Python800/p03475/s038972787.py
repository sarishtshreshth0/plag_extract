import sys
input = sys.stdin.readline
import numpy as np

 
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

n = I()
mylist = [list(MI()) for i in range(n-1)]

def main(j):
    time = 0
    for i in range(j,n-1):
        c, s, f = mylist[i]
        if time < s:
            time = s
        if (time - s) % f != 0:
            time += (f - (time - s) % f) #待ち時間を足す
        time += c
    print(time)
    
    
for i in range(n-1):
    main(i)
print(0)
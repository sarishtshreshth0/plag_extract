from collections import defaultdict
import bisect

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

q,h,s,d = readInts()
n = readInt()

reasonable = [-1,-1]
value = {"0.25":q,"0.5":h,"1":s,"2":d}
t = min(8*q,4*h,2*s,d)
if t==8*q:
  reasonable = [0.25,q]
  ans = (n//reasonable[0])*reasonable[1]
  print(int(ans))
elif t==4*h:
  reasonable = [0.5,h]
  ans = (n//reasonable[0])*reasonable[1]
  print(int(ans))
elif t==2*s:
  reasonable = [1,s]
  ans = (n//reasonable[0])*reasonable[1]
  print(ans)
else:
  reasonable = [2,d]
  remain = n%2
  money = 0
  if remain==1:
    money = min(4*q,2*h,1*s)
  print(int(money)+(n//reasonable[0])*reasonable[1])

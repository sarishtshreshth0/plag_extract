import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  s=S()
  t=S()

  ns=len(s)
  nt=len(t)

  dp=[[0]*(ns+1) for _ in range(nt+1)]

  for i in range(nt):
    for j in range(ns):
      if t[i]==s[j]:
        dp[i+1][j+1]=dp[i][j]+1
      else:
        dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])

  ans=[]
  i=nt
  j=ns
  while dp[i][j]!=0:
    if dp[i][j]==dp[i-1][j]:
      i-=1
    elif dp[i][j]==dp[i][j-1]:
      j-=1
    elif dp[i][j]==dp[i-1][j-1]:
      i-=1
      j-=1
    elif dp[i][j]==dp[i-1][j-1]+1:
      i-=1
      j-=1
      ans.append(t[i])

  ans.reverse()
  return ''.join(ans)

# main()
print(main())

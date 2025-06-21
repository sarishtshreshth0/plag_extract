import math
def main():
  n=int(input())
  w = list(map(int,input().split()))
  ans=abs(sum(w[:1])-sum(w[1:]))
  for t in range(2,n+1):
    if ans>abs(sum(w[:t])-sum(w[t:])):
      ans=abs(sum(w[:t])-sum(w[t:]))
  print(ans)

main()
def main():
  n,k = list(map(int,input().split()))
  ans=0
  while n>0:
    ans+=1
    n=int(n/k)
  print(ans)
main()
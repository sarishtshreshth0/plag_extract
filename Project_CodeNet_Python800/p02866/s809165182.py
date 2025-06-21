def main():
  from collections import Counter
  M=998244353
  n,*d=map(int,open(0).read().split())
  e=Counter(d)
  a=1if d[0]<1==e[0]else 0
  for i in range(n):a*=pow(e[i],e[i+1],M)
  print(a%M)
main()
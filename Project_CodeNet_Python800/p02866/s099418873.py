def main():
  n,*d=map(int,open(0).read().split())
  e=[0]*n
  for i in d:e[i]+=1
  a=1if d[0]<1else 0
  for i in d[1:]:a=a*e[i-1]%998244353
  print(a)
main()
def main():
  n=int(input())
  s=input()
  sl,sr=[0],[0]# sl:(,  sr:)
  l,r=0,0
  for si in s:
    if si=='(':
      l+=1
    else:
      r+=1
    sr.append(r)
    sl.append(l)
  ans=n
  al,ar=0,0
  for i in range(n):
    if s[i]=='(':
      a=(sl[n]-sl[i+1])-(ar+sr[n]-sr[i+1])
      if a>=0:
        ar+=a+1
    else:
      a=sr[i]-(al+sl[i+1])
      if a>=0:
        al+=a+1
  print('('*al+s+')'*ar)
if __name__=='__main__':
  main()
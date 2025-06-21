a,b=map(int,input().split())

if a%2==0:
  if b%2==0:
    c=((b-1)//2-a//2+1)%2
    if c==0:
      print(b)
    else:
      if b%2==0:
        print(b+1)
      else:
        print(b-1)
  else:
    print((b//2-a//2+1)%2)
else:
  if b%2==0:
    c=(b//2-a//2-1)%2
    ans=list(format(b,"b")[::-1])
    ans[0]=str((int(ans[0])+c)%2)
    for i,x in enumerate(format(a,"b")[::-1]):
      ans[i]=str((int(ans[i])+int(x))%2)

    ans=str("0b"+"".join(ans[::-1]))
    print(int(ans,0))
    
  else:
    c=(b//2-(a+1)//2+1)%2
    if c==0:
      print(a)
    else:
      if a%2==0:
        print(a+1)
      else:
        print(a-1)
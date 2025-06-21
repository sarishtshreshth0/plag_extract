n,a,b=map(int,input().split())
s=str(input())
s=list(s)
for i in range(len(s)):
  if s[i]=="a" and a+b>0:
    print("Yes")
    if a>0:
      a=a-1
    else:
      b=b-1
  elif s[i]=="b" and b>0:
    print("Yes")
    b=b-1
  else:
    print("No")
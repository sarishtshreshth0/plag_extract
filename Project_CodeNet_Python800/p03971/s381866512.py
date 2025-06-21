N,A,B=map(int,input().split())
s=input()
kaigai=1
jyun=1
for i in range(N):
  if s[i]=="c":
    print("No")
  elif s[i]=="a":
    if jyun<=A+B:
      print("Yes")
      jyun+=1
    else:
      print("No")
  else:
    if jyun<=A+B and kaigai<=B:
      print("Yes")
      kaigai+=1
      jyun+=1
    else:
      print("No")
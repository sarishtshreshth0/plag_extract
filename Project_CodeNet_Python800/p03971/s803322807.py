N,A,B=map(int,input().split())
S=input()
pass_a=1
pass_b=1
for x in S:
  if x=="a":
    if pass_a<=A+B:
      print("Yes")
      pass_a+=1
    else:
      print("No")
  elif x=="b":
    if pass_a<=A+B and pass_b<=B:
      print("Yes")
      pass_a+=1
      pass_b+=1
    else:
      print("No")
  else:
    print("No")

N,A,B = [ int(i) for i in input().split() ]
S = input()

passCount = 0
overseaPassCount = 1
for k,v in enumerate(S):
  if v == "c":
    print("No")
  elif v == "b":
    if passCount<A+B and overseaPassCount<=B :
      print("Yes")
      overseaPassCount += 1
      passCount += 1
    else:
      print("No")
  elif v == "a":
    if passCount<A+B :
      print("Yes")
      passCount += 1
    else:
      print("No")

  else :
    None


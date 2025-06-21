A,B,C = map(int,input().split())

maxi=max(A,B,C)
mini=min(A,B,C)
if C!=maxi and C!=mini:
  print("Yes")
else:
  print("No")
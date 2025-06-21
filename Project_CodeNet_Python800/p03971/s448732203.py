n,A,B=map(int,input().split())
contestant=list(input())
aa=0
bb=0
for i in range(n):
  if contestant[i]=="c":
    print("No")
  elif contestant[i]=="b":
    if aa+bb<A+B and bb<B:
      print("Yes")
      bb+=1
    else:
      print("No")
    
  elif contestant[i]=="a":
    if aa+bb<A+B:
      print("Yes")
    else:
      print("No")
    aa+=1

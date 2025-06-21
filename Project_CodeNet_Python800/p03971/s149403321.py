datalist=list(map(int,input().split()))
N, A, B = datalist[0], datalist[1], datalist[2]
strings=str(input())
na,nb=0,0
out=[]
for i in range(len(strings)):
  if strings[i]=="a":
    if na + nb < A+B:
      out.append("Yes")
      na += 1
    else:
      out.append("No")
  elif strings[i]=="b":
    if na + nb < A+B:
      if nb < B:
        out.append("Yes")
        nb += 1
      else:
        out.append("No")
    else:
      out.append("No")
  else:
    out.append("No")
print("\n".join(out))

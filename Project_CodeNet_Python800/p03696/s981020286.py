n=int(input())
s=input()
d=[0]*n
lcount=0
rcount=0
for i in range(len(s)):
  if s[i]=="(":
    lcount+=1
  else:
    if lcount>=1:
      lcount-=1
    else:
      rcount+=1

print("("*rcount+s+")"*lcount)
n,a,b=map(int,input().split())
s=input()
cnt=0
cntt=0
for i in range(n):
  if s[i]=="a":
    if cnt+1<=a+b:
      cnt+=1
      print("Yes")
    else:
      print("No")
  if s[i]=="b":
    if cnt+1<=a+b and cntt+1<=b:
      cnt+=1
      cntt+=1
      print("Yes")
    else:
      print("No")
  if s[i]=="c":
    print("No")
n,a,b=input().split(" ")
n=int(n)
a=int(a)
b=int(b)
lst=input()
cnt=0
cnt2=0
for i in range(n):
  if lst[i]=="a":
    if cnt<a+b:
      print("Yes")
      cnt+=1
    else:
      print("No")
  elif lst[i]=="b":
    if cnt<a+b and cnt2<b:
      print("Yes")
      cnt+=1
      cnt2+=1
    else:
      print("No")
  else:
    print("No")
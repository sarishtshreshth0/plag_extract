n,a,b = map(int, input().split())
s = input()
ya=0
yb=0
for c in s:
  if c=="a" and ya+yb<a+b:
    print("Yes")
    ya+=1
  elif c=="b"and ya+yb<a+b and yb<b:
    print("Yes")
    yb+=1
  else:
    print("No")
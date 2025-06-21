n,a,b = map(int,input().split())
s = input()
y = 0
bn = 1
for i in range(n):
  if s[i] == "a" and y < a + b:
    print("Yes")
    y += 1
  elif s[i] == "b" and y < a + b and bn <= b:
    print("Yes")
    y += 1
    bn += 1
  else:
    print("No")
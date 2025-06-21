N,A,B=map(int,input().split())
s=str(input())
x = 0 #通過者数
y = 0
count = 0
for i in range(len(s)):
  if s[i] == 'a' and x+y < A+B:
    print('Yes')
    x += 1
  elif s[i] == 'b' and x+y < A+B and y < B:
    print('Yes')
    y += 1
  else:
      print('No')
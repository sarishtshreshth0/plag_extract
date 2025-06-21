NN =input().split()
a = int(NN[0])
b = int(NN[1])
c = int(NN[2])
d = int(NN[3])
list1=[a,b,c,d]
list1.sort()
ans = list1[2] -list1[1]
if b < c or d < a:
  print(0)
else:
  print(ans)
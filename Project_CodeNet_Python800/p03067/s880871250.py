# -*- coding: utf-8 -*-


#----------
a,b,c = [int(i) for i in input().rstrip().split()]
#----------

if ((a <= c) and (c <= b)) or ((b <= c) and (c <= a)):
  print("Yes")
else:
  print("No")

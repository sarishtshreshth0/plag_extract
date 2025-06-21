# -*- coding: utf-8 -*-


#----------
a,b,c = [int(i) for i in input().rstrip().split()]
#----------

#if ((a <= c) and (c <= b)) or ((b <= c) and (c <= a)):
#  print("Yes")
#else:
#  print("No")

# 距離で判定してみる
if ( abs(b-a) > abs(c-a) ) and ( abs(b-a) > abs(c-b) ):
  print("Yes")
else:
  print("No")

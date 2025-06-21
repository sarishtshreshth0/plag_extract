A, B = map(int, input().split())

def cumxor(P):
  x = P % 4
  if x == 0:
    return P
  elif x == 1:
    return 1
  elif x == 2:
    return P+1
  else:
    return 0

if A == B:
  print(A)
elif A == 0:
  print(cumxor(B))
else:
  print(cumxor(A-1) ^ cumxor(B))

# 試した
#def cumxor(P):
#  ret = 0
#  for i in range(0,P+1):
#    ret = ret ^ i
#  return ret 
#for i in range(0,130):
#  cx = cumxor(i)
#  print(i, cx, bin(i), bin(cx))


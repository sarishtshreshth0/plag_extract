N, A, B = map(int, input().split())
S = input()

import sys

T = A + B
Ta = B

for p in S:
  if p == "c":
    print("No")
    continue
    
  elif p == "a":
    if T > 0:
      print("Yes")
      T -= 1
    else:
      print("No")
      
  else:
    if T > 0 and Ta > 0:
      print("Yes")
      Ta -= 1
      T -= 1
    else:
      print("No")

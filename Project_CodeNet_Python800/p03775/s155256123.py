import math as ma
N = int (input ())
n = ma.floor(int(ma.sqrt(N)))
while 1 < n+1:
  if (N/n)%1 == 0:
    x = str(N/n)
    print (len(x)-2)
    break
  else:
    n -= 1
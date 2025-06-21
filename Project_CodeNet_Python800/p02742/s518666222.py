H,W = [int(i) for i in input().split()]

h1 = H//2
h2 = H-h1

w2 = W//2
w1 = W-w2

if H==1 or W==1:
  print(1)
else:
  print(h2*w1+h1*w2)
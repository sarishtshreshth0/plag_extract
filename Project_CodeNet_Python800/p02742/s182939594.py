from sys import stdin

h, w = [int(x) for x in stdin.readline().strip().split()]
if(h == 1 or w == 1):
  print(1)
else:
  print((h//2)*(w//2)+((h+1)//2)*((w+1)//2))
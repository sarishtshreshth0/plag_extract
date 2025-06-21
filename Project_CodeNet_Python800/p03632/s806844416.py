A, B, C, D = list(map(lambda t: int(t), input().split(" ")))
 
if B - A + D - C <= max([D - A, B - C]):
  print(0)
else:
  print(min([B, D]) - max([A, C]))
import sys
import math
X,Y = map(int,input().split())

if not (1 <= X <= 100 and 1 <= Y <= 100): sys.exit()
if not (Y % 2 == 0): sys.exit()

print(X+math.floor(Y/2))

# ABC160-B

import sys
def I(): return int(sys.stdin.readline().rstrip())

X = I()
print(1000*(X//500) + 5*((X % 500)//5))

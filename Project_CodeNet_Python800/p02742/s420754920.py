il = [int(k) for k in input().split()]

H = il[0]
W = il[1]
# H : 縦
#  W : 横

import math

a = math.ceil(W/2)
b = math.floor(W/2)
c = math.ceil(H/2)
d = math.floor(H/2)

if H == 1 or W == 1:
    print("1")
else:
    print(a*c + b*d)

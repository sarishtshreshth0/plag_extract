from math import *
def gcd2(array):
    temp = array[0]
    for a in array[1:]:
        temp = gcd(temp, a)
    return temp
N, X = map(int, input().split())
D = []
for x in map(int, input().split()):
    D.append(abs(x-X))
print(gcd2(D))


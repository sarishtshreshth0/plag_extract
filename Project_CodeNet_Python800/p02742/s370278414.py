from math import ceil
H,W=map(int,input().split())
print(ceil(H*W/2) if H!=1 and W!=1 else 1)
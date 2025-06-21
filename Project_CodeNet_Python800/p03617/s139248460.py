import sys
input = sys.stdin.readline
from collections import *

Q, H, S, D = map(int, input().split())
N = int(input())
S = min(S, 4*Q, 2*H)
D = min(D, 8*Q, 4*H, 2*S)
print(N//2*D+N%2*S)
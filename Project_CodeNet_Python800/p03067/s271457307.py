import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


A,B,C = MI()
print('Yes' if A < C < B or B < C < A else 'No')

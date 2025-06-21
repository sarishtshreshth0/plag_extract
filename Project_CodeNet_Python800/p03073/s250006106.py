import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))

S = LI2()
N = len(S)
print(min(sum(S[i] for i in range(0,N,2)) + sum(1-S[i] for i in range(1,N,2)),sum(1-S[i] for i in range(0,N,2))+sum(S[i] for i in range(1,N,2))))

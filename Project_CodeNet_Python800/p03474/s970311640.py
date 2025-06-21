import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


A,B = MI()
S = LS2()

for i in range(A+B+1):
    if i == A:
        if S[i] != '-':
            print('No')
            break
    else:
        if S[i] == '-':
            print('No')
            break
else:
    print('Yes')

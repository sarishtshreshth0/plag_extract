import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    m,d=map(int,input().split())
    cnt=0
    for i in range(10,d+1):
        if int(str(i)[0])>=2 and int(str(i)[1])>=2 and 1<=int(str(i)[0])*int(str(i)[1])<=m:
            cnt+=1
    print(cnt)
        
    
resolve()
MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def main():
    x,y = map(int,input().split())
    print(x + y//2)
if __name__ =='__main__':
    main()   

import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,m = LI()
    x = LI()
    x.sort()
    lst = []

    for i in range(1,m):
        lst.append(x[i]-x[i-1])
    
    lst.sort(reverse=True)
    ans = sum(lst[n-1:])
    print(ans)
main()            

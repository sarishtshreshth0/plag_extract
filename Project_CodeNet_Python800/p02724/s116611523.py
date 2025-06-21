def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())
import sys
sys.setrecursionlimit(10**6)

n=int(input())
k=(n//500)*1000
t=((n%(500))//5)*5
print(k+t)
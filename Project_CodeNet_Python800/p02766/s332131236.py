import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def conv_num2x(num, x):
    if (int(num/x)):
        return conv_num2x(int(num/x), x)+str(num%x)
    return str(num%x)

def main():
    N,K = LI()
    num_k = conv_num2x(N,K)
    print(len(str(num_k)))

main()


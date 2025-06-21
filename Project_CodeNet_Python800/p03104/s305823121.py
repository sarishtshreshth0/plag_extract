import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
#N = I()
#A = [LI() for _ in range(N)]

a,b = MI()

if a % 2 == 0:
    if b % 2 == 0:
        if (b-a) % 4 == 2:
            print(b + 1)
        else:
            print(b)
    else:
        if (b-a) % 4 == 1:
            print(1)
        else:
            print(0)
else:
    if b % 2 == 0:
        if (b-a) % 4 == 1:
            bst = bin(b)
            ast = bin(a)
            anst = '0b'
            if len(bst) - len(ast) > 0:
                for i in range(len(bst) - len(ast)):

                    anst += bst[2+i]
            for i in range(len(ast) -2):
                if ast[-len(ast) + 2 + i] == bst[-len(ast) + 2 + i]:
                    anst += '0'
                else:
                    anst += '1'
                aa = int(anst[2:],2)
            print(aa)

        else:
            bst = bin(b)
            ast = bin(a)
            anst = '0b'
            if len(bst) - len(ast) > 0:
                for i in range(len(bst) - len(ast)):
                    anst += bst[2 + i]
            for i in range(len(ast) - 2):
                if ast[-len(ast) + 2 + i] == bst[-len(ast) + 2 + i]:
                    anst += '0'
                else:
                    anst += '1'
                aa = int(anst[2:], 2)
            print(aa - 1)
    else:
        if (b-a) % 4 == 2:
            print(a-1)
        else:
            print(a)
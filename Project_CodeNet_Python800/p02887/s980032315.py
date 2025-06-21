import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N=ii()
    S=list(input())

    pre = None
    X = []
    for s in S:
        if s != pre:
            X.append(s)

        pre = s
    
    print(len(X))






if __name__ == "__main__":
    main()
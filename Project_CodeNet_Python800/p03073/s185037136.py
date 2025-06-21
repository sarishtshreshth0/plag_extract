import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF = 10**20
def main():
    S=list(input())
    N=len(S)

    A,B=[],[]
    pre = "0"
    for i in range(N):
        if pre == "0":
            new = "1"
        else:
            new = "0"
        A.append(new)
        pre = new
        
    pre = "1"
    for i in range(N):
        if pre == "0":
            new = "1"
        else:
            new = "0"
        B.append(new)
        pre = new

    ans = INF
    for X in [A,B]:
        count = 0
        for i in range(N):
            if S[i] != X[i]:
                count += 1

        ans = min(ans,count)

    print(ans)





if __name__ == "__main__":
    main()
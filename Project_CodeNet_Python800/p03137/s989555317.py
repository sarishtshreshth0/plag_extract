
def solve():
    if N >= M:
        return 0
    elif N == 1:
        cnt = abs(X[-1] - X[0])
        return cnt
    L = [0] * (M-1)
    
    for i in range(len(L)):
        L[i] = X[i+1] - X[i]
    L.sort()
    return sum(L[:M-N])



if __name__=="__main__":
    N,M = list(map(int, input().split()))
    X = list(map(int, input().split()))
    X.sort()
    print(solve())

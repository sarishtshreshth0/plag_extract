#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

def lcs(X,Y):
    m,n = len(X),len(Y)
    L = [[0]*(n+1) for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    size = L[m][n] 
    lcs = []
    i,j = m,n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]: 
            lcs.append(X[i-1]) 
            i-=1
            j-=1
        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
    return ''.join(lcs[::-1])

s = input().strip()
t = input().strip()
ans = lcs(s,t)
print(ans)
    

N = int(input())
L = [input() for _ in range(N)]
print("Yes" if L.count(L[0])==1 and all(L.count(L[i])==1 \
                  and L[i][0]==L[i-1][-1] for i in range(1, N)) else "No")
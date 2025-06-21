def resolve():
    N = int(input())
    W = [input() for _ in range(N)]
    used = []
    for i in range(1, N):
        if W[i-1][-1] != W[i][0] or W[i] in used:
            print("No")
            return 
        used.append(W[i-1])
    print("Yes")




if '__main__' == __name__:
    resolve()
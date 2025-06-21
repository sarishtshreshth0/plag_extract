def resolve():
    N = int(input())
    W = [input() for _ in range(N)]
    if len(set(W)) != N:
        print("No")
        return
    l = W[0][0]
    for w in W:
        if w[0] != l:
            print("No")
            return
        l = w[-1]
    print("Yes")

resolve()
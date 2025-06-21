def resolve():
    N, M = [int(i) for i in input().split()]
    S = input().split(sep="-")
    if len(S) != 2 or len(S[0]) != N or len(S[1]) != M:
        print("No")
    else:
        print("Yes")


resolve()

def resolve():
    N, A, B = [int(i) for i in input().split()]
    S = input()
    ac = 0
    abc = 0
    for s in S:
        flg = False
        if s == "a":
            if ac < A + B:
                flg = True
                ac += 1
        elif s == "b":
            if ac < A + B and abc < B:
                flg = True
                ac += 1
                abc += 1
        else:
            pass

        if flg:
            print("Yes")
        else:
            print("No")


resolve()

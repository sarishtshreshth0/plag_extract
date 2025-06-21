N, A, B = map(int, input().split())
S = input()

qual = {"A": 0, "B": 0}

for i in range(N):
    ans = False
    l = S[i]
    if qual["A"] + qual["B"] < A + B:
        if l == "a":
            ans = True
            qual["A"] += 1
        elif l == "b":
            if qual["B"] < B:
                ans = True
                qual["B"] += 1
    if ans:
        print('Yes')
    else:
        print('No')
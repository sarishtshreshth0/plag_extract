N,A,B = map(int,input().split())
S = input()
f = []
ok = 0
for i,s in enumerate(S):
    if s == "a":
        if ok < A + B:
            print("Yes")
            ok += 1
        else:
            print("No")
    elif s == "b":
        if ok < A + B and len(f) + 1 <= B:
            print("Yes")
            ok += 1
            f.append(i)
        else:
            print("No")
    else:
        print("No")
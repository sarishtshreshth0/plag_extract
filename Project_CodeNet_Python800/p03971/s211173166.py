N,A,B = map(int, input().split())
S = input()

C,D = 0,0
for i,c in enumerate(S):
    if c == 'a':
        if C < A+B:
            print("Yes")
            C += 1
        else:
            print("No")
    elif c == 'b':
        if C < A+B and D < B:
            print("Yes")
            C += 1
            D += 1
        else:
            print("No")
    else:
        print("No")
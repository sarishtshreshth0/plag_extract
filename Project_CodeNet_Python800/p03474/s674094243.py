A, B = map(int, input().split())
S = input()

if(S[A] == "-"):
    S = S[:A] + S[A+1:]
    if(S.isdecimal()):
        print("Yes")
    else:
        print("No")
else:
    print("No")

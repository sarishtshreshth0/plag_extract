A,B = map(int,input().split())
flag = 0
S = list(input())
if S[A] != "-":
    print("No")
else:
    if "".join(S[:A]).isdigit() and "".join(S[A+1:]).isdigit():
        print("Yes")
    else:
        print("No")
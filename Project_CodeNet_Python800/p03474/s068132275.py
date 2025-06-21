A, B = map(int, input().split())
S = input().strip()
try:
    if int(S[:A]) >= 0 and int(S[-B:]) >= 0 and S[A] == "-":
        print("Yes")
    else:
        print("No")
except:
    print("No")

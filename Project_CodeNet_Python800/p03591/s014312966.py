S = list(input())
if len(S)>3:
    if S[0] == "Y":
        if S[1] == "A":
            if S[2] == "K":
                if S[3] == "I":
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
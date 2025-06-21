N,A,B = map(int,input().split())
S = input()
pas = 0
num = A + B
kaigai = 0
for i in range(len(S)):
    if S[i] == "a":
        if pas < num:
            pas += 1
            print("Yes")
        else:
            print("No")
    elif S[i] == "b":
        kaigai += 1
        if pas < num and kaigai <= B:
            pas += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")


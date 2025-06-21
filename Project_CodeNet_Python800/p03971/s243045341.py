#3
N,A,B = map(int,input().split())
S = input()
cou = 0
coub = 0

for i in range(N):
    if S[i] == "a":
        if  cou < (A+B):
            print("Yes")
            cou += 1
        else:
            print("No")
    elif S[i] == "b":
        coub += 1
        if cou < (A+B) and coub <= B:
            print("Yes")
            cou += 1
        else:
            print("No")
    else:
        print("No")

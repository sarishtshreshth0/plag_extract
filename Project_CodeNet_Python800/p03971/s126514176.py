N,A,B = map(int, input().split())
S = ["*"]+list(input())

finalist = 0
foreigner_student_finalist = 0

for i in range(1,N+1):
    if S[i] == "a":
        if finalist < A+B:
            print("Yes")
            finalist += 1
        else:
            print("No")
    elif S[i] == "b":
        if finalist < A+B and foreigner_student_finalist < B:
            print("Yes")
            finalist += 1
            foreigner_student_finalist += 1
        else:
            print("No")
    else:
        print("No")
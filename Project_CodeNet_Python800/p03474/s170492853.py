A,B = map(int,input().split())
S = input().strip()
Num = [str(i) for i in range(10)]
if S[A]=="-":
    flag = 0
    for i in range(A+B+1):
        if i!=A and S[i] not in Num:
            flag = 1
            break
    if flag==0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
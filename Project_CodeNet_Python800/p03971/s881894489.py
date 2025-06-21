Input = list(map(int,input().split()))
S = input()

N = Input[0]
A = Input[1]
B = Input[2]
Pass = 0
B_Pass = 0
for iter in range(N):
    if S[iter] == 'a' and Pass < A+B:
        Pass += 1
        print("Yes")
    elif S[iter] == 'b' and Pass < A+B and B_Pass < B:
        Pass += 1
        B_Pass += 1
        print("Yes")
    else:
        print("No")
    

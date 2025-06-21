N, A, B = map(int, input().split())
S = input()
count = 0
count2 = 0


for i in range(N):
    if S[i] == "c":
        print("No")
    elif S[i] == "a":
        
        if count < A+B:
            print("Yes")
            count += 1
        else:
            print("No")
    elif S[i] == "b":
        
        if count < A+B and count2 < B:
            print("Yes")
            count += 1
            count2 += 1
        else:
            print("No")
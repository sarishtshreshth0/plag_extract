N, A, B = map(int, input().split())
S = list(input())
count = 0
b_rank = 1
for i in range(len(S)) :
    if S[i] == "a" :
        if count < A + B :
            print("Yes")
            count += 1
        else :
            print("No")
    if S[i] == "b" :
        if count < A + B and b_rank <= B :
            print("Yes")
            count += 1
            b_rank += 1
        else :
            print("No")
    if S[i] == "c" :
        print("No")

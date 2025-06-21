import sys
a = [int(c) for c in input().split()]
N = a[0]
A = a[1]
B = a[2]
S = input()

cnt = 0
f = 0

for i in range(N):
    if S[i] == "a":
        if cnt < A+B:
           print("Yes")
           cnt+=1 
        else:
            print("No")
    elif S[i] == "b":
        if cnt < A+B and f+1 <= B:
            print("Yes")
            cnt+=1
            f+=1
        else:
            print("No")
        pass
    elif S[i] == "c":
        print("No")

N, A, B = map(int,input().split())
S = input()
yosen = 0
yosen_b = 1
for i in range(N):
    if S[i] == "a" and yosen < (A + B):
            print("Yes")
            yosen += 1
    elif S[i] == "b" and yosen < (A + B) and yosen_b <= B:
            print("Yes")
            yosen += 1
            yosen_b += 1
    else:
        print("No")
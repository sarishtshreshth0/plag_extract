N, A, B = map(int, input().split())
S = input()

ps = A + B
a,b = 0,0
for i in range(N):
    if S[i] == "c" or a >= ps:
        print("No")
        continue
    if S[i] == "b":
        b += 1
        if b > B:
            print("No")
            continue
    a += 1
    print("Yes")
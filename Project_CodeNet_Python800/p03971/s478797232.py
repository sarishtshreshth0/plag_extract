N, A, B = map(int, input().split())
s = input()

x = A + B
cnt = 1
rank = 1
for i in range(N):
    y = s[i : i+1]
    if cnt <= x:
        if y == "a":
            print("Yes")
            cnt += 1
        elif y == "b" and rank <= B:
            print("Yes")
            cnt += 1
            rank += 1
        else:
            print("No")
    else:
        print("No")
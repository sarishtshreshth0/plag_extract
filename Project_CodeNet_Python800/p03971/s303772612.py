N, A, B = map(int, input().split())
S = list(input())
ans = ""
cnt = 0
f = 0

for i in range(len(S)):
    if S[i] == "c":
        ans = "No"
    elif S[i] == "a":
        if cnt < A + B:
            ans = "Yes"
            cnt += 1
        else:
            ans = "No"
    elif S[i] == "b":
        if cnt < A + B and f < B:
            ans = "Yes"
            cnt += 1
            f += 1
        else:
            ans = "No"
    print(ans)

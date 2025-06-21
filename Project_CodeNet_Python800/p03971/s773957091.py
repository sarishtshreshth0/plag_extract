N,A,B = map(int, input().split())
S = list(input())
cnt_all = 0
cnt_over = 0
for i in range(N):
    if S[i] == 'a':
        if cnt_all < A+B:
            print("Yes")
            cnt_all += 1
        else:
            print("No")
    elif S[i] == 'b':
        if cnt_all < A+B and cnt_over < B:
            print("Yes")
            cnt_all += 1
            cnt_over += 1
        else:
            print("No")
    else:
        print("No")
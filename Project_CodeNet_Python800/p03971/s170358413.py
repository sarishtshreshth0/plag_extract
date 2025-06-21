N,A,B=map(int,input().split())
A += B
cnt = [0,0]
S=list(input())
for i in range(N):
    if S[i] == 'c':
        print("No")
    elif S[i] == 'a':
        if cnt[0] < A:
            print("Yes")
            cnt[0] += 1
        else:
            print("No")
    else:
        if cnt[0] < A and cnt[1] < B:
            print("Yes")
            cnt[0] += 1
        else:
            print("No")
        cnt[1] += 1
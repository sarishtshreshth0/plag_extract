N,A,B = map(int,input().split())
S = input().strip()
cnt = 0
cnt2 = 0
for i in range(N):
    if S[i]=="c":
        print("No")
        continue
    if S[i]=="a":
        if cnt<A+B:
            print("Yes")
            cnt += 1
        else:
            print("No")
    elif S[i]=="b":
        if cnt<A+B and cnt2<B:
            print("Yes")
            cnt += 1
            cnt2 += 1
        else:
            print("No")
            cnt2 += 1
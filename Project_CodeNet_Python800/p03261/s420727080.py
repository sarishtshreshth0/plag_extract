N = int(input())
dic = dict()
for i in range(N):
    S = input()
    if S in dic:
        dic[S] += 1
    else:
        dic[S] = 1
    Start  = S[0]
    if i != 0:
        if Start != End or dic[S] > 1:
            print("No")
            exit()
    End = S[len(S)-1]
print("Yes")
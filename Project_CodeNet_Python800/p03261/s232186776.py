N = int(input())
W = [input() for i in range(N)]
if(len(set(W)) == N):
    if(all([W[i-1][-1] == W[i][0] for i in range(1, N)])):
        print("Yes")
    else:
        print("No")
else:
    print("No")

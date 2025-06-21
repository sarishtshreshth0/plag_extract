def main():
    N = int(input())
    S = []
    for _ in range(N-1):
        c,s,f = map(int,input().split())
        S.append([c,s,f])

    for i in range(N-1):
        t = S[i][1] + S[i][0]
        for j in range(i+1,N-1):
            t = max(S[j][1],-(-t//S[j][2])*S[j][2]) + S[j][0]

        print(t)

    print(0)


main()
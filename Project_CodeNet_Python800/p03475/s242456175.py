from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N=int(readline())
    C=[0]*(N-1)
    S=[0]*(N-1)
    F=[0]*(N-1)
    for i in range(N-1):
        C[i],S[i],F[i]=map(int,readline().split())

    for i in range(N):
        if i==N-1:
            print(0)
            break
        for j in range(i,N-1):
            if j==i:
                t=S[j]+C[j]
            else:
                if t<S[j]:
                    t+=S[j]-t
                else:
                    t+=(S[j]-t)%F[j]
                t+=C[j]
        print(t)

if __name__=="__main__":
    main()
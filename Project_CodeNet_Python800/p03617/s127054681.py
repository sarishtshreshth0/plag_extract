def main():
    Q,H,S,D=map(int,input().split())
    N=int(input())
    S=min(S,2*(min(H,2*Q))) # lowest price
    print(S*N if 2*S<=D else (N//2)*D+(N%2)*S)

main()
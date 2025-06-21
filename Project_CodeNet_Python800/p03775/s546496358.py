def main():
    from math import sqrt
    N=int(input())
    sqrtN=int(sqrt(N))
    div=[d for d in range(1,sqrtN+1) if N%d==0]
    ans=100
    for d in div:
        e=0
        for e in range(12):
            if (N//d)<10**e:
                ans=min(ans,e)
    print(ans)

if __name__=='__main__':
    main()

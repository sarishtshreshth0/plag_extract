def main():
    n=int(input())
    x=list(map(int, input().split()))
    d=[]
    rui=0
    kei=sum(x)
    for i in range(n-1):
        rui += x[i]
        d.append( abs(rui - (kei - rui)) )
    print(min(d))
    
if __name__ == "__main__":
    main()
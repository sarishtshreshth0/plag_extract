def main():
    n = int(input())
    inlis = list()
    for _ in range(n-1):
        c, s, f= map(int, input().split())
        inlis.append([c, s, f])

    anslis = []

    for j in range(n-1):
        tmp = 0
        for i in range(j,n-1):
            c, s, f= inlis[i][0], inlis[i][1], inlis[i][2]
            if tmp < s:
                tmp = s
            
            amari = tmp % f
            if amari != 0:
                tmp += f - amari

            tmp += c
            #print(j, c, s, f, amari, tmp)
        anslis.append(tmp)
    anslis.append(0)
    
    for k in anslis:
        print(k)
    


if __name__ == "__main__":
    main()

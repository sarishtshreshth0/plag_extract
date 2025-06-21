def main():
    n,d =map(int,input().split())
    X = []
    for i in range(n):
        tmp = [int(i) for i in input().split()]
        X.append(tmp)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            s = 0
            for k in range(d):
                s += (X[i][k]-X[j][k])**2
            s = s**0.5
            #print(s)
            if s.is_integer():
                ans += 1
    print(ans)
main()
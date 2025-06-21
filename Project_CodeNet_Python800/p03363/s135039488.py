def main():
    n = int(input())
    a = list(map(int,input().split()))

    # ruiseki
    rui = [0]*(n+1)
    for i in range(n):
        rui[i+1] = rui[i] + a[i]
    from collections import Counter
    c = Counter(rui)
    
    # Query
    res = 0
    for v in c.values():
        res += v*(v-1)//2
    print(res)

if __name__ == '__main__':
    main()

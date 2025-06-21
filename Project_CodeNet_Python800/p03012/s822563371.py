def main():
    n = int(input())
    inlis = list(map(int, input().split()))
    
    tmp = 10**10

    for i in range(1,n):
        sa = abs(sum(inlis[:i]) - sum(inlis[i:]))
        if sa <= tmp:
            tmp = sa
    print(tmp)

    
if __name__ == "__main__":
    main()

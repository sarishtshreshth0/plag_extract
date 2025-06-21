def main():
    from collections import defaultdict
    N = int(input())
    A = [0] * N
    cumsum = 0
    dic = defaultdict(int)
    zero = 0
    for i, a in enumerate([int(x) for x in input().split()]):
        cumsum += a
        dic[cumsum] += 1
        A[i] = cumsum

    ans = zero * (zero + 1) // 2
    for a, b in dic.items():
        if a == 0:
            ans += b * (b + 1) // 2
        else:
            ans += b * (b - 1) // 2
    
    print(ans)

if __name__ == '__main__':
    main()
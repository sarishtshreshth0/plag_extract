def solve():
    n = int(input())
    w = list(map(int, input().split()))
    dif = 1000
    for i in range(len(w)):
        dif = min(dif, abs(sum(w[:i]) - sum(w[i:])))
    print(dif)





if __name__ == '__main__':
    solve()

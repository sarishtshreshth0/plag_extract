from math import ceil
from operator import itemgetter

def main():
    N = int(input())
    AB = [list(map(int,input().split())) for _ in range(N)]
    CD = [list(map(int,input().split())) for _ in range(N)]
    AB.sort( key = itemgetter(1))
    AB.sort(key = itemgetter(0))
    CD.sort( key = itemgetter(0))
    CD.sort(key = itemgetter(1))

    ans = 0
    used = [False]*N
    for i in range(N):
        c,d = CD[i]
        for j in range(N):
            a,b = AB[N - j - 1]
            if not(used[N - j - 1]) and a <= c and b <= d:
                ans += 1
                used[N - j - 1] = True
                break
    print(ans)
    return

if __name__ == "__main__":
    main()
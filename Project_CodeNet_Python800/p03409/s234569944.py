INF = float("inf") #const
MOD = 10**9+7 #const
MAX = 510000 #const

import fractions
import itertools

def main():
    n = int(input())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab = sorted(ab,key=lambda x:x[1],reverse=True)
    cd = [list(map(int,input().split())) for _ in range(n)]
    cd = sorted(cd,key=lambda x:x[0])

    ans = 0
    for blue in cd:
        for red in ab:
            if red[0] < blue[0] and red[1] < blue[1]:
                ans += 1
                red[1] = 201
                break

    print(ans)


if __name__ == "__main__":
    main()

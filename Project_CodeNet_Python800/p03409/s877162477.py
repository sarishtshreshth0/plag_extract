import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    N = int(input())
    reds = [tuple(map(int, input().split())) for _ in range(N)]
    blues = [tuple(map(int, input().split())) for _ in range(N)]
    cnt = 0

    blues = sorted(blues, key=lambda x: x[0])
    for i in blues:
        temp = (-1, -1)

        for j in reds:
            if j[0] < i[0] and j[1] < i[1]:
                if j[1] > temp[1]:
                    temp = (j[0], j[1])
                    tempind = j
        if temp != (-1, -1):
            cnt += 1
            # blues.remove(i)
            reds.remove(tempind)
    print(cnt)


resolve()
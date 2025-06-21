import sys
import itertools
sys.setrecursionlimit(10000)
def resolve():
    N = int(input())
    Reds = sorted([list(map(int, input().split(" "))) for i in range(N)], key=lambda x: x[1], reverse=True)
    Blues = sorted([list(map(int, input().split(" "))) for i in range(N)], key=lambda x: x[0])
    used = []
    for red in Reds:
        for blue in Blues:
            if blue not in used and able_to_be_pair(red, blue):
                used.append(blue)
                break
    print(len(used))

def able_to_be_pair(red, blue):
    return True if (blue[0] - red[0]) > 0 and (blue[1] - red[1]) > 0 else False

if '__main__' == __name__:
    resolve()
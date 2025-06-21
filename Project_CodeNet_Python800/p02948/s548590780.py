import sys

# import bisect
# map(int, sys.stdin.read().split())
from collections import Counter
import heapq
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def main():
    N,M = map(int,input().split())
    A =[]
    for i in range(N):
        a,b = map(int,input().split())
        A.append((a,-b))
    A.sort()
    A = deque(A)

    h = []
    ans =0
    for i in range(1,M+1):

        while A:
            if A[0][0] ==i:
                temp = A.popleft()
                heapq.heappush(h,temp[1])
            else:
                break

        if len(h)==0:
            continue
        else:
            ans += heapq.heappop(h)


    print(-ans)







if __name__ == "__main__":
    main()

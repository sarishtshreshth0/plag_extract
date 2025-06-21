import sys
from collections import deque
sys.setrecursionlimit(1000000) # 再帰上限を増やす

def main():
    input = sys.stdin.readline  # 文字列に対してinputした場合は、rstripするのを忘れずに！
    N = int(input())
    red = []
    for _ in range(N):
        a, b = map(int, input().rstrip().split())
        red.append((a, b))
    blue = []
    for _ in range(N):
        c, d = map(int, input().rstrip().split())
        blue.append((c, d))
    red.sort(key=lambda x:x[1], reverse=True)
    blue.sort()

    count = 0
    blue = deque(blue)
    used = set()
    for b in blue:
        for i, r in enumerate(red):
            if i not in used:
                if r[0] < b[0] and r[1] < b[1]:
                    count += 1
                    used.add(i)
                    break
    print(count)

if __name__ == '__main__':
    main()
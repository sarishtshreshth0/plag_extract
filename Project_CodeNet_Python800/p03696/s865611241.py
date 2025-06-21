import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    S = input()
    height = 0
    deepest = 0
    for c in S:
        if c == '(':
            height += 1
        else:
            height -= 1
        deepest = min(deepest, height)
    ans = '(' * (-deepest) + S + ')' * (height - deepest)
    print(ans)

if __name__ == "__main__":
    main()

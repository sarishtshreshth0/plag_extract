import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from collections import Counter
def main():
    n, *a = map(int, read().split())
    ac = Counter(a)
    acs = sorted(ac.items())
    r = ac.most_common()[0][1]
    if len(acs) == 2:
        if acs[1][0] - acs[0][0] == 1:
            r = acs[0][1] + acs[1][1]

    for i1 in range(1, len(acs) - 1):
        if abs(acs[i1 - 1][0] - acs[i1+1][0]) <= 2:
            r = max(r, acs[i1-1][1] + acs[i1][1] + acs[i1+1][1])
        elif abs(acs[i1 - 1][0] - acs[i1][0]) <= 1:
            r = max(r, acs[i1-1][1] + acs[i1][1])
        elif abs(acs[i1 + 1][0] - acs[i1][0]) <= 1:
            r = max(r, acs[i1+1][1] + acs[i1][1])
    print(r)
if __name__ == '__main__':
    main()

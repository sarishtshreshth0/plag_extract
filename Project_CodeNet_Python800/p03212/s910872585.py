from itertools import product
from bisect import bisect_right
def main():
    n = int(input())
    n_753 = []
    for i in range(3, 10):
        for s in product(['3', '5', '7'], repeat = i):
            if len(set(s)) != 3:
                continue
            n_753.append(int(''.join(s)))
    n_753.sort()
    print(bisect_right(n_753, n))
if __name__ == '__main__':
    main()

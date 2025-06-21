import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))
MIIZ = lambda: list(map(lambda x: x-1, MII()))

def main():
    a, b = MII()
    cards = [2,3,4,5,6,7,8,9,0,11,12,13,1]
    i_a = cards.index(a)
    i_b = cards.index(b)
    if i_a == i_b: print('Draw')
    elif i_a > i_b: print('Alice')
    else: print('Bob')

if __name__ == '__main__':
    main()

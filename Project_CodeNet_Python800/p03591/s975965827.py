from sys import stdin

in_strings = lambda: stdin.readline()[:-1] # s = in_strings()
in_int = lambda: int(stdin.readline()) # N = in_int()
in_intlist = lambda: list(map(int, stdin.readline().split())) # List = in_intlist()

S = in_strings()
if S[:4] == 'YAKI':
    print('Yes')
else:
    print('No')

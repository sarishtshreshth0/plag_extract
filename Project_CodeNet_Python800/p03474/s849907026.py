import sys
import copy
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b = map(int, input().split())
s = input().split("-")

if len(s) == 2 and len(s[0]) == a and len(s[1]) == b:
    print('Yes')
    sys.exit()
else: print('No')
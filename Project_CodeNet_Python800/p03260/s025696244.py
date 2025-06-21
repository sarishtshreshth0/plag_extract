import sys

rm = lambda: map(int, sys.stdin.buffer.readline().split())

a, b = rm()
print('No' if a == 2 or b == 2 else 'Yes')
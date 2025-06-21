import sys

s = sys.stdin.readline().strip()

if len(s) >= 4 and s[:4] == 'YAKI':
    sys.stdout.write('Yes')
else:
    sys.stdout.write('No')
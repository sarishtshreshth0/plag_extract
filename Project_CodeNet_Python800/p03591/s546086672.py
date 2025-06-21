import sys, re
input = sys.stdin.readline
pattern = re.compile('YAKI')

m = pattern.match(input())
print('Yes' if m else 'No')


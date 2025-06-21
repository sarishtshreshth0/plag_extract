import re

A, B = map(int, input().split())
S = input()
print ('Yes' if re.search(r'\A\d{{{}}}-\d{{{}}}\Z'.format(A, B), S) else 'No') 
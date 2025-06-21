import re
A, B = (int(x) for x in input().split())
S = input()
match = '\d' * A + '-' + '\d' * B 
ptn = re.compile(match)
print('Yes' if ptn.search(S) != None else 'No')
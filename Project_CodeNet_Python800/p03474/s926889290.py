import re
A,B=map(int,input().split())
S=input()

m = re.match(r'^(\d+)\-(\d+)$', S)

if m:
    if len(m.groups()[0]) == A and len(m.groups()[1]) == B:
        print('Yes')
    else:
        print('No')
else:
    print('No')

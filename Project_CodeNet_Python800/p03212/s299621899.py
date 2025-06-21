import itertools
import bisect

lis = list(itertools.product('7530',repeat = 9))
int_lis = list(map(int,map(''.join,lis)))
str_lis = list(map(str,int_lis[:-16]))
lis = []
for s in str_lis:
    if ('7' in s) and ('5' in s) and ('3' in s) and ('0' not in s) :
        lis.append(int(s))
print(bisect.bisect_right(sorted(lis),int(input())))

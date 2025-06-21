abc = list(map(int,input().split()))
abc_s = sorted(abc)
if abc[2]==abc_s[1]: print('Yes')
else: print('No')
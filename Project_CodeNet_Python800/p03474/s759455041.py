import sys,re
input = sys.stdin.readline

a,b=list(map(int,input().split()))
s=input().rstrip()
rs = r"\d"*a+"-"+"\d"*b
print('Yes'if re.match(rs,s) else 'No')

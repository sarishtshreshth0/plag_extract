import sys
input=sys.stdin.readline

n,m=map(int,input().split())
if n>=m:
    print(0)
    exit()

lst=sorted(map(int,input().split()))
sa=[]
for i in range(m-1):
    sa.append(lst[i+1]-lst[i])
sa=sorted(sa)
print(sum(sa[:m-n]))
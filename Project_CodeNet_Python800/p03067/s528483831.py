def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
a,b,c = iim()

if a<c<b or b<c<a: print('Yes')
else: print('No')
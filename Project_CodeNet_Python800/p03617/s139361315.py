q,h,s,d = map(int,input().split())
#20 30 70 90
N = int(input())
#3


o = min(q*4,h*2,s)

if o*2 <= d:
	print(o*N)
else:
	print(d*(N//2) + o*(N%2))
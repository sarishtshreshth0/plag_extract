n,*w=map(int,open(0).read().split())
s=10**9
sum_w=sum(w)
for i in range(1,n):
	s=min(s,abs(sum_w-2*sum(w[:i])))
print(s) 
n=int(input())
w=list(map(int,input().split()))
c,d,e=0,sum(w),sum(w)
for i in range(n):
  c+=w[i]
  d-=w[i]
  e=min(e,abs(c-d))
print(e)
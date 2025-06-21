s=raw_input().strip()
t=raw_input().strip()
n=len(s)
m=len(t)
z=[[0]*(m+1) for _ in xrange(n+1)]
for i in xrange(n):
    for j in xrange(m):
        if s[i]==t[j]:
            z[i+1][j+1]=z[i][j]+1
        else:
            z[i+1][j+1]=max(z[i+1][j],z[i][j+1])
i=n-1
j=m-1
a=[]
while i>=0 and j>=0:
    if s[i]==t[j]:
        a.append(s[i])
        i-=1
        j-=1
    elif z[i][j+1]>z[i+1][j]:
        i-=1
    else:
        j-=1
print ''.join(a[::-1])
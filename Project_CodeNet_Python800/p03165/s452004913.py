def lcs(s1,s2,m,n,t):
    l=[]
    for i in range(0,m+1):
        t[i][0]=0
    for i in range(1,n+1):
        t[0][i]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    i=m
    j=n
    while(i>0 and j>0):
        if s1[i-1]==s2[j-1]:
            l.append(s1[i-1])
            i-=1
            j-=1
        else:
            if t[i-1][j]>t[i][j-1]:
                i-=1
            else:
                j-=1
    l.reverse()  
    if len(l)==0:b=""
    else:b="".join(str(a) for a in l)
    return b
s1=input()
s2=input()
m=len(s1)
n=len(s2)
t=[[0 for x in range(n+1)] for x in range(m+1)] 
d=lcs(s1,s2,m,n,t)
print(d)
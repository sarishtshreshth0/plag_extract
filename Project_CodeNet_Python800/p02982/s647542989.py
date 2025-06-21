n,d = [int(z) for z in input().split()]
p=[]
for g in range(n):
      p.append([int(z) for z in input().split()])
c=0

def dist(a,b):
      s=0
      for i in range(d):
            s+= (a[i]-b[i])**2
      return s**0.5

for j in range(n):
      for k in range(j+1,n):
            z = dist(p[j],p[k])
            #print(z)
            if (type(z)==float)or(type(z)==int):
                       if (z%1==0):
                             c+=1
print(c)

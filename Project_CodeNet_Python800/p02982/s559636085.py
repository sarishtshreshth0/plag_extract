n, d=map(int, input().split())

a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])


s_list=[]

for i in range(n-1):
    for j in range(i+1, n):
        
        sum=0
        for k in range(d):
            sum+=(a[i][k]-a[j][k])**2
        s_list.append(sum)
        
#max
num=int(max(s_list)**(1/2))

count=0
for i in range(num+1):
    for j in s_list:
        if j==i**2:
            count+=1
            
print(count)
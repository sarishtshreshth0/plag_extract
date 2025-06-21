import math

n=int(input())

#a<bとすると、aの最大値は
amax=int(math.sqrt(n))

total=[]

for i in range(1,amax+1):
    if n%i==0:
        b=n//i
        total.append(len(str(b)))
        
print(min(total))
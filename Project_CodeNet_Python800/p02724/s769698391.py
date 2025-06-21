x=int(input())
i=0
u=0
while 500<=x:
    x-=500
    i+=1
while x>=5:
    x-=5
    u+=1
print(1000*i+5*u)
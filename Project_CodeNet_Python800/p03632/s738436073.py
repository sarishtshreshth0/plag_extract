A,B,C,D = map(int,input().split())
Alice=False
Bob=False
time=0
for i in range(101):
    if i==A:
        Alice=True
    if i==B:
        Alice=False
    if i==C:
        Bob=True
    if i==D:
        Bob=False
    if Alice==True and Bob==True:
        time+=1
print(time)
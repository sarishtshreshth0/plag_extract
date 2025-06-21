x=int(input())
gohyaku=0
goen=0
while x>5:
    x-=500
    gohyaku+=1
if x==5:
    goen+=1
elif 0<=x<5:
    pass
elif x<0:
    x+=500
    gohyaku-=1
    while x>=5:
        goen+=1
        x-=5
print(gohyaku*1000+goen*5)
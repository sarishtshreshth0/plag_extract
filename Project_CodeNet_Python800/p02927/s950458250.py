m,d = map(int,input().split())
cn = 0

for i in range(1,d+1):
    tt = 0
    if((i%10)>=2 and i//10>=2):
        tt = (i%10)*(i//10)
    if(tt<=m and tt>=1):
        cn+=1
        #print(i%10,i//10)
    
print(cn)
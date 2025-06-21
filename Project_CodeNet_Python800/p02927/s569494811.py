M,D = map(int,input().split())
num = 0
for i in range(1,M+1):
        for j in range(22,D+1):
                lis = list(str(j))

                if int(lis[0])<=1 or int(lis[1])<=1:
                        lis =[]
                        continue
                if int(lis[0])*int(lis[1]) == i:
                        num+=1
                lis =[]                
print(num)

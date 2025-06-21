import math
M,D=map(int,input().split())
days=[]
count = 0
divisors = []
for k in range(1,M+1):
    for i in range(22,D+1):
        if int(str(i)[0])>=2 and int(str(i)[1])>=2:
            if k==int(str(i)[0])*int(str(i)[1]):
                count += 1
print(count)

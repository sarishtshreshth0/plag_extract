M,D=map(int,input().split())

count=0

for n in range(22,D+1):
    if (n//10)*(n%10)<=M and n%10>=2:
        count +=1

print(count)

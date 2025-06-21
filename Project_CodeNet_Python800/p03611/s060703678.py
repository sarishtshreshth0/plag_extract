kouho = [0]*(10**5+3)#-1は+2に格納

N = int(input())
a = list(map(int,input().split()))

for i in range(0,N,1):
    kouho[a[i]]+=1
    kouho[a[i]-1]+=1
    kouho[a[i]+1]+=1

print(max(kouho))

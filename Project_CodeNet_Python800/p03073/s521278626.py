s=list(input())
n=len(s)
count1=0
for i in range(1,n+1):
    if int(s[i-1])!=(i%2):
        count1+=1
count2=0
for j in range(n):
    if int(s[j])!=j%2:
        count2+=1
print(min(count1,count2))

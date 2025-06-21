N = int(input())
S = list(input())
check = S[0]
count =1
for i in range(1,N):
    if(check!=S[i]):
        check=S[i]
        count +=1
print(count)
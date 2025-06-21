from collections import Counter
N = int(input())
a = list(map(int,input().split()))
count_list = [0]*(10**5+1)
ans = 0
for i in a:
    count_list[i]+=1
for i in range(1,10**5):
    ans = max(ans,(count_list[i-1]+count_list[i]+count_list[i+1]))
print(ans)
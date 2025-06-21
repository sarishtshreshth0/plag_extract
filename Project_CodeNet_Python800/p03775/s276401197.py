import math

n = int(input())
ans_list = []

for i in range(1,int(math.sqrt(n))+1):
    if n%i == 0:
        ans_list.append(max(len(str(n//i)),len(str(i))))

print(min(ans_list))
